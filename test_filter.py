product_class = indexes.MultiValueField(null=True, faceted=True)


def prepare_product_class(self, obj):
    attributes = obj.attributes.all()
    if len(attributes) > 0:
        return [product_class.type for product_class in attributes]

    class Meta:
        model = ProductAttribute
        fields = ["name", "code", "type", "option_group", "required"]