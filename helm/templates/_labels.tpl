{{/*
Common labels
*/}}
{{- define "chart.labels" -}}
app.kubernetes.io/instance: {{ .Release.Name }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
app.kubernetes.io/name: {{ include "helm.name" . }}
helm.sh/chart: {{ include "helm.chart" . }}
{{ toYaml .Values.labels | trimSuffix "\n" }}
{{- end -}}
