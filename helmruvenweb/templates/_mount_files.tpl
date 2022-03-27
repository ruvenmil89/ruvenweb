{{/*
Config map for exampl file
*/}}
{{- define "helmruvenweb.configmapexample" -}}
{{- if .Values.examplefile }}
apiVersion: v1
kind: ConfigMap
metadata:
  name: {{ .Release.Name }}-example-conf
data:
  {{- $files := .Files }}
  {{- range tuple "examplemountfile.py" }}
  {{ . }}: |-
        {{ $files.Get . }}
  {{- end }}
{{- end }}
{{- end }}

{{/*
Create volume for topology ConfigMap.
*/}}
{{- define "helmruvenweb.exampleFileVolume" }}
{{- if .Values.examplefile }}
- name: example-file
  configMap:
    name: {{ template "helmruvenweb.configmapexample" . }}
{{- end }}
{{- end }}

{{/*
Create volume mount for topology ConfigMap.
*/}}
{{- define "helmruvenweb.exampleFileVolumeMount" }}
{{- if .Values.examplefile }}
- mountPath: /opt/app/scripts
  name: example-file
  readOnly: true
{{- end }}
{{- end }}
