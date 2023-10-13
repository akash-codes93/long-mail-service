{{/*
Define pullsecret name
*/}}
{{- define "chart.pullSecretName" -}}
{{- $fullName := include "helm.fullname" . -}}
{{- printf "%s-%s" $fullName "pullsecret" | replace "+" "_" | trunc 63 | trimSuffix "-" -}}
{{- end }}
