{{/* vim: set filetype=mustache: */}}
{{/*
Generate a common value to set selectors
*/}}
{{- define "chart.selectors" -}}
app.kubernetes.io/instance: {{ .Release.Name }}
app.kubernetes.io/name: {{ include "helm.name" . }}
{{- end -}}