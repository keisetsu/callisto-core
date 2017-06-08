from wizard_builder.admin import (
    FormQuestionChildAdmin, FormQuestionParentAdmin, MultipleChoiceChildAdmin,
    MultipleChoiceParentAdmin,
)
from wizard_builder.models import (
    Checkbox, Date, FormQuestion, MultiLineText, MultipleChoice, RadioButton,
    SingleLineText, SingleLineTextWithMap,
)

from django.contrib import admin

from .models import EvaluationField


class EvalFieldInline(admin.StackedInline):
    model = EvaluationField


class WithEval(object):

    def __init__(self, *args, **kwargs):
        super(WithEval, self).__init__(*args, **kwargs)
        self.inlines = (self.inlines or []) + [EvalFieldInline, ]


class FormQuestionParentWithEvalAdmin(WithEval, FormQuestionParentAdmin):
    pass


class FormQuestionChildWithEvalAdmin(WithEval, FormQuestionChildAdmin):
    pass


class MultipleChoiceParentWithEvalAdmin(WithEval, MultipleChoiceParentAdmin):
    pass


class MultipleChoiceChildWithEvalAdmin(WithEval, MultipleChoiceChildAdmin):
    pass


admin.site.unregister(FormQuestion)
admin.site.unregister(SingleLineText)
admin.site.unregister(SingleLineTextWithMap)
admin.site.unregister(MultiLineText)
admin.site.unregister(Date)

admin.site.register(FormQuestion, FormQuestionParentWithEvalAdmin)
admin.site.register(SingleLineText, FormQuestionChildWithEvalAdmin)
admin.site.register(SingleLineTextWithMap, FormQuestionChildWithEvalAdmin)
admin.site.register(MultiLineText, FormQuestionChildWithEvalAdmin)
admin.site.register(Date, FormQuestionChildWithEvalAdmin)

admin.site.unregister(MultipleChoice)
admin.site.unregister(Checkbox)
admin.site.unregister(RadioButton)

admin.site.register(MultipleChoice, MultipleChoiceParentWithEvalAdmin)
admin.site.register(Checkbox, MultipleChoiceChildWithEvalAdmin)
admin.site.register(RadioButton, MultipleChoiceChildWithEvalAdmin)
