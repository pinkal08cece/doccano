from django.urls import include, path

from .views import (annotation, annotation_relations, auto_labeling, comment,
                    example, example_state, export_dataset, health,
                    import_dataset, import_export, label, project,
                    relation_types, role, statistics, tag, task, user)
from .views.tasks import category, span, text

urlpatterns_project = [
    path(
        route='upload',
        view=import_dataset.UploadAPI.as_view(),
        name='upload'
    ),
    path(
        route='catalog',
        view=import_dataset.DatasetCatalog.as_view(),
        name='catalog'
    ),
    path(
        route='download-format',
        view=export_dataset.DownloadDatasetCatalog.as_view(),
        name='download-format'
    ),
    path(
        route='download',
        view=export_dataset.DownloadAPI.as_view(),
        name='download-dataset'
    ),
    path(
        route='statistics',
        view=statistics.StatisticsAPI.as_view(),
        name='statistics'),
    # path(
    #     route='labels',
    #     view=label.LabelList.as_view(),
    #     name='label_list'
    # ),
    # path(
    #     route='label-upload',
    #     view=label.LabelUploadAPI.as_view(),
    #     name='label_upload'
    # ),
    # path(
    #     route='labels/<int:label_id>',
    #     view=label.LabelDetail.as_view(),
    #     name='label_detail'
    # ),
    path(
        route='category-types',
        view=label.DocTypeList.as_view(),
        name='doc_types'
    ),
    path(
        route='category-types/<int:label_id>',
        view=label.DocTypeDetail.as_view(),
        name='doc_type'
    ),
    path(
        route='span-types',
        view=label.SpanTypeList.as_view(),
        name='span_types'
    ),
    path(
        route='span-types/<int:label_id>',
        view=label.SpanTypeDetail.as_view(),
        name='span_type'
    ),
    path(
        route='category-type-upload',
        view=label.DocTypeUploadAPI.as_view(),
        name='doc_type_upload'
    ),
    path(
        route='span-type-upload',
        view=label.SpanTypeUploadAPI.as_view(),
        name='span_type_upload'
    ),
    path(
        route='examples',
        view=example.ExampleList.as_view(),
        name='example_list'
    ),
    path(
        route='examples/<int:example_id>',
        view=example.ExampleDetail.as_view(),
        name='example_detail'
    ),
    path(
        route='relation_types',
        view=relation_types.RelationTypesList.as_view(),
        name='relation_types_list'
    ),
    path(
        route='relation_type-upload',
        view=relation_types.RelationTypesUploadAPI.as_view(),
        name='relation_type-upload'
    ),
    path(
        route='relation_types/<int:relation_type_id>',
        view=relation_types.RelationTypesDetail.as_view(),
        name='relation_type_detail'
    ),
    path(
        route='annotation_relations',
        view=annotation_relations.AnnotationRelationsList.as_view(),
        name='relation_types_list'
    ),
    path(
        route='annotation_relation-upload',
        view=annotation_relations.AnnotationRelationsUploadAPI.as_view(),
        name='annotation_relation-upload'
    ),
    path(
        route='annotation_relations/<int:annotation_relation_id>',
        view=annotation_relations.AnnotationRelationsDetail.as_view(),
        name='annotation_relation_detail'
    ),
    # Todo: remove.
    path(
        route='docs',
        view=example.DocumentList.as_view(),
        name='doc_list'
    ),
    path(
        route='docs/<int:doc_id>',
        view=example.DocumentDetail.as_view(),
        name='doc_detail'
    ),
    path(
        route='approval/<int:example_id>',
        view=annotation.ApprovalAPI.as_view(),
        name='approve_labels'
    ),
    # Todo: change.
    path(
        route='docs/<int:doc_id>/annotations',
        view=annotation.AnnotationList.as_view(),
        name='annotation_list'
    ),
    path(
        route='docs/<int:doc_id>/annotations/<int:annotation_id>',
        view=annotation.AnnotationDetail.as_view(),
        name='annotation_detail'
    ),
    path(
        route='examples/<int:example_id>/categories',
        view=category.CategoryListAPI.as_view(),
        name='category_list'
    ),
    path(
        route='examples/<int:example_id>/categories/<int:annotation_id>',
        view=category.CategoryDetailAPI.as_view(),
        name='category_detail'
    ),
    path(
        route='examples/<int:example_id>/spans',
        view=span.SpanListAPI.as_view(),
        name='span_list'
    ),
    path(
        route='examples/<int:example_id>/spans/<int:annotation_id>',
        view=span.SpanDetailAPI.as_view(),
        name='span_detail'
    ),
    path(
        route='examples/<int:example_id>/texts',
        view=text.TextLabelListAPI.as_view(),
        name='text_list'
    ),
    path(
        route='examples/<int:example_id>/texts/<int:annotation_id>',
        view=text.TextLabelDetailAPI.as_view(),
        name='text_detail'
    ),
    path(
        route='tags',
        view=tag.TagList.as_view(),
        name='tag_list'
    ),
    path(
        route='tags/<int:tag_id>',
        view=tag.TagDetail.as_view(),
        name='tag_detail'
    ),
    path(
        route='examples/<int:example_id>/comments',
        view=comment.CommentListDoc.as_view(),
        name='comment_list_doc'
    ),
    path(
        route='comments',
        view=comment.CommentListProject.as_view(),
        name='comment_list_project'
    ),
    path(
        route='examples/<int:example_id>/comments/<int:comment_id>',
        view=comment.CommentDetail.as_view(),
        name='comment_detail'
    ),
    path(
      route='examples/<int:example_id>/states',
      view=example_state.ExampleStateList.as_view(),
      name='example_state_list'
    ),
    path(
        route='roles',
        view=role.RoleMappingList.as_view(),
        name='rolemapping_list'
    ),
    path(
        route='roles/<int:rolemapping_id>',
        view=role.RoleMappingDetail.as_view(),
        name='rolemapping_detail'
    ),
    path(
        route='auto-labeling-templates',
        view=auto_labeling.AutoLabelingTemplateListAPI.as_view(),
        name='auto_labeling_templates'
    ),
    path(
        route='auto-labeling-templates/<str:option_name>',
        view=auto_labeling.AutoLabelingTemplateDetailAPI.as_view(),
        name='auto_labeling_template'
    ),
    path(
        route='auto-labeling-configs',
        view=auto_labeling.AutoLabelingConfigList.as_view(),
        name='auto_labeling_configs'
    ),
    path(
        route='auto-labeling-configs/<int:config_id>',
        view=auto_labeling.AutoLabelingConfigDetail.as_view(),
        name='auto_labeling_config'
    ),
    path(
        route='auto-labeling-config-testing',
        view=auto_labeling.AutoLabelingConfigTest.as_view(),
        name='auto_labeling_config_test'
    ),
    path(
        route='examples/<int:example_id>/auto-labeling',
        view=auto_labeling.AutoLabelingAnnotation.as_view(),
        name='auto_labeling_annotation'
    ),
    path(
        route='auto-labeling-parameter-testing',
        view=auto_labeling.AutoLabelingConfigParameterTest.as_view(),
        name='auto_labeling_parameter_testing'
    ),
    path(
        route='auto-labeling-template-testing',
        view=auto_labeling.AutoLabelingTemplateTest.as_view(),
        name='auto_labeling_template_test'
    ),
    path(
        route='auto-labeling-mapping-testing',
        view=auto_labeling.AutoLabelingMappingTest.as_view(),
        name='auto_labeling_mapping_test'
    )
]

urlpatterns = [
    path(
        route='health',
        view=health.Health.as_view(),
        name='health'
    ),
    path('auth/', include('dj_rest_auth.urls')),
    path('fp/', include('django_drf_filepond.urls')),
    path(
        route='me',
        view=user.Me.as_view(),
        name='me'
    ),
    path(
        route='features',
        view=import_export.Features.as_view(),
        name='features'
    ),
    path(
        route='projects',
        view=project.ProjectList.as_view(),
        name='project_list'
    ),
    path(
        route='users',
        view=user.Users.as_view(),
        name='user_list'
    ),
    path(
        route='roles',
        view=role.Roles.as_view(),
        name='roles'
    ),
    path(
        route='tasks/status/<task_id>',
        view=task.TaskStatus.as_view(),
        name='task_status'
    ),
    path(
        route='projects/<int:project_id>',
        view=project.ProjectDetail.as_view(),
        name='project_detail'
    ),
    path('projects/<int:project_id>/', include(urlpatterns_project))
]
