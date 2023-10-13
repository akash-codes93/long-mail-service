{{/* vim: set filetype=mustache: */}}

{{/*
Define secret name to store secret environment variables
*/}}
{{- define "chart.envsecretsname" -}}
{{- $fullName := include "helm.fullname" . -}}
{{- printf "%s-%s" $fullName "envsecret" | replace "+" "_" | trunc 63 | trimSuffix "-" -}}
{{- end }}

{{/*
Define configmap name to store configuration files.
*/}}
{{- define "chart.configfilesname" -}}
{{- $fullName := include "helm.fullname" . -}}
{{- printf "%s-%s" $fullName "configfiles" | replace "+" "_" | trunc 63 | trimSuffix "-" -}}
{{- end }}

{{/*
Define secret name to store secrets in files.
*/}}
{{- define "chart.filesecretsname" -}}
{{- $fullName := include "helm.fullname" . -}}
{{- printf "%s-%s" $fullName "fsecret" | replace "+" "_" | trunc 63 | trimSuffix "-" -}}
{{- end }}

{{/*
Define SecretStore name for External Secrets
*/}}
{{- define "chart.secretstore" -}}
{{- $fullName := include "helm.fullname" . -}}
{{- printf "%s-%s" $fullName "secretstore" | replace "+" "_" | trunc 63 | trimSuffix "-" -}}
{{- end }}

{{/*
Define ExternalSecret name for External Secrets
*/}}
{{- define "chart.externalsecret" -}}
{{- $fullName := include "helm.fullname" . -}}
{{- printf "%s-%s" $fullName "externalsecret" | replace "+" "_" | trunc 63 | trimSuffix "-" -}}
{{- end }}

{{/*
Define secret name to store secret environment variables from external secret operator
*/}}
{{- define "chart.extSecret" -}}
{{- $fullName := include "helm.fullname" . -}}
{{- printf "%s" $fullName | replace "+" "_" | trunc 63 | trimSuffix "-" -}}
{{- end }}
