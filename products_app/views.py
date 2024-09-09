from rest_framework import serializers, permissions, status, response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.viewsets import ModelViewSet
from .models import ProductCategory, ProductModel
from .serializers import ProductCategorySerializer, ProductSerializer, ProductDetailSerializer

class ProductCategoryViewSet(ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    
    def get_permissions(self):
        if self.request.method == "GET":
            return [permissions.AllowAny()]
        return [permissions.IsAdminUser()]
    

class ProductViewSet(ModelViewSet):
    queryset = ProductModel.objects.all()
    

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ProductDetailSerializer
        return ProductSerializer
    
    def get_permissions(self):
        if self.request.method == "GET":
            return [permissions.AllowAny()]
        return [permissions.IsAdminUser()]
    

    def get_queryset(self):
        name = self.request.GET.get('name', '')
        category = self.request.GET.get('category', '')


        queryset = ProductModel.objects.filter(status=True)

        if name:
            queryset = queryset.filter(product_name__icontains=name)
        
        if category:
            queryset = queryset.filter(product_category__category_name=category)
        
        return queryset.order_by('-addition_date')
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.status = False
        instance.save()
        
        return response.Response({'message': 'Product status updated to inactive.'}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([permissions.IsAdminUser])
def get_inactive_products(request):
    products = ProductModel.objects.filter(status=False).order_by('-addition_date')

    serializer = ProductSerializer(products, many=True)

    return response.Response({
        "products": serializer.data
    })