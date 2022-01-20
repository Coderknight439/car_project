import django_tables2 as tables


class PartiesTable(tables.Table):
    id = tables.Column(visible=False)
    full_name = tables.Column(verbose_name="Full name")
    user_type = tables.Column(verbose_name="Party Type")

    actions = tables.TemplateColumn(template_name='parties/table_actions.html', orderable=False)
    
    def render_user_type(self, record):
        if record.is_operator:
            return 'Operator'
        elif record.is_manager:
            return 'Manager'

    class Meta:
        attrs = {"class": "table table-vcenter card-table"}
