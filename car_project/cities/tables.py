import django_tables2 as tables
from .models import CityCars


class CityTable(tables.Table):
    id = tables.Column(visible=False)
    name = tables.Column(verbose_name="Name")
    code = tables.Column(verbose_name="Code")

    actions = tables.TemplateColumn(template_name='cities/table_actions.html', orderable=False)

    class Meta:
        attrs = {"class": "table table-vcenter card-table"}


class CityCarTable(tables.Table):
    id = tables.Column(visible=False)
    city = tables.Column(verbose_name="City")
    car = tables.Column(verbose_name="Car")
    operator = tables.Column(verbose_name="Operator")
    operator_code = tables.Column(verbose_name="Operator Code", accessor='operator_code')
    
    def render_city(self, record):
        if record.city:
            return record.city.name
    
    def render_car(self, record):
        if record.car:
            return record.car.name
    
    def render_operator(self, record):
        if record.operator:
            return record.operator.full_name
    
    def render_operator_code(self, record):
        if record.operator:
            return record.operator.code
    
    class Meta:
        attrs = {"class": "table table-vcenter card-table"}
        fields = ['id', 'city', 'car', 'operator', 'operator_code']
        model = CityCars

