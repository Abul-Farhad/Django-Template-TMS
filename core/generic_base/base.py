# views/base.py
from rest_framework.generics import ListAPIView
from django.http import StreamingHttpResponse
import csv
from rest_framework.response import Response
import time

class Echo:
    """Helper class to stream CSV lines as they are written."""
    def write(self, value):
        return value


class BaseListAPIViewWithCSVExport(ListAPIView):
    export_csv_serializer_class = None  # Must be defined in child
    csv_filename = 'data.csv'  # Default filename
    def get_queryset(self):
        # queryset = super().get_queryset()
        queryset = self.queryset
        
        # Handle DataTables ordering
        order_column_index = self.request.GET.get('order[0][column]')
        order_dir = self.request.GET.get('order[0][dir]', 'asc')
        # print("#####################################################")
        # print("\t\tPrinting Query Params")
        # print("#####################################################")

        # for key, val in self.request.GET.items():
        #     print(f"{key}: {val}")

        if order_column_index is not None:
            try:
                field_name = self.column_mapping[int(order_column_index)]
                if order_dir == 'desc':
                    field_name = '-' + field_name
                queryset = queryset.order_by(field_name)
            except (IndexError, ValueError, KeyError):
                pass

        return queryset

    def list(self, request, *args, **kwargs):
        if request.GET.get('export') == 'csv':
            return self.export_as_csv(request)

        queryset = self.filter_queryset(self.get_queryset())

        draw = int(request.GET.get('draw', 1))
        start = int(request.GET.get('start', 0))
        length = int(request.GET.get('length', 10))
    

        total_records = self.queryset.count()
        filtered_records = queryset.count()

        page = queryset[start:start+length]
        serializer = self.get_serializer(page, many=True)
        
        return Response({
            'draw': draw,
            'recordsTotal': total_records,
            'recordsFiltered': filtered_records,
            'data': serializer.data
        })
    
    # def get_paginated_response(self, data):
    #     if self.request.GET.get('export') == 'csv':
    #         return Response(data)
    #     return super().get_paginated_response(data)


    def export_as_csv(self, request):
        start = time.time()
        queryset = self.filter_queryset(self.get_queryset())
        # print(f"Filtered queryset in {time.time() - start:.2f}s")  # <--- Add this
        pseudo_buffer = Echo()
        writer = csv.writer(pseudo_buffer)

        response = StreamingHttpResponse(
            self.stream_queryset_rows(queryset, writer),
            content_type='text/csv'
        )
        response['Content-Disposition'] = f'attachment; filename="{self.csv_filename}"'
        return response

    def stream_queryset_rows(self, queryset, writer):
        # Yield header manually (match fields as needed)
        # print("Parent class stream_queryset_rows method called")
        headers = self.column_mapping.values()
        yield writer.writerow(headers)

        for user in queryset.iterator(chunk_size=1000):

            row = [getattr(user, field, None) for field in headers]
                    
            yield writer.writerow(
                row
                
                
            )
            # user.name,
                # user.email,
                # 'Yes' if user.is_staff else 'No',
                # 'Yes' if user.is_superuser else 'No',
                # user.role.name if user.role else '—'

