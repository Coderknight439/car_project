import django_tables2 as tables


class CarsTable(tables.Table):
    id = tables.Column(visible=False)
    name = tables.Column(verbose_name="Name")
    code = tables.Column(verbose_name="Code")

    actions = tables.TemplateColumn(template_name='cars/table_actions.html', orderable=False)

    class Meta:
        attrs = {"class": "table table-vcenter card-table"}
