"""Code snippet templates per language for corpus generation."""

from __future__ import annotations

CODE_SNIPPETS: dict[str, str] = {
    "python": '''```python
from typing import Any

class {class_name}:
    """{docstring}"""

    def __init__(self, config: dict[str, Any]) -> None:
        self._config = config

    def process(self, payload: dict[str, Any]) -> dict[str, Any]:
        return {{"status": "ok", "topic": "{topic}", "variant": {variant}}}
```''',
    "java": '''```java
public class {class_name} {{
    private final String topic = "{topic}";
    private final int variant = {variant};

    public Record<String, Object> process(Map<String, Object> payload) {{
        return Map.of("status", "ok", "topic", topic, "variant", variant);
    }}
}}
```''',
    "javascript": '''```javascript
export async function {function_name}(config) {{
  const {{ topic = "{topic}", variant = {variant} }} = config;
  return {{ status: "ok", topic, variant }};
}}
```''',
    "typescript": '''```typescript
interface {interface_name}Config {{
  topic: string;
  variant: number;
}}

export async function {function_name}(config: {interface_name}Config): Promise<Record<string, unknown>> {{
  return {{ status: "ok", topic: config.topic, variant: config.variant }};
}}
```''',
    "csharp": '''```csharp
public class {class_name}
{{
    public string Topic {{ get; }} = "{topic}";
    public int Variant {{ get; }} = {variant};

    public Dictionary<string, object> Process(Dictionary<string, object> payload)
        => new() {{ ["status"] = "ok", ["topic"] = Topic, ["variant"] = Variant }};
}}
```''',
    "cpp": '''```cpp
#include <string>
#include <unordered_map>

class {class_name} {{
public:
    std::unordered_map<std::string, std::string> process() {{
        return {{{{"status", "ok"}}, {{"topic", "{topic}"}}, {{"variant", std::to_string({variant})}}}};
    }}
}};
```''',
    "go": '''```go
package main

type {class_name} struct {{
    Topic   string
    Variant int
}}

func (s *{class_name}) Process() map[string]interface{{}} {{
    return map[string]interface{{}}{{"status": "ok", "topic": "{topic}", "variant": {variant}}}
}}
```''',
    "rust": '''```rust
pub struct {class_name} {{
    pub topic: String,
    pub variant: u32,
}}

impl {class_name} {{
    pub fn process(&self) -> serde_json::Value {{
        serde_json::json!({{"status": "ok", "topic": self.topic, "variant": self.variant}})
    }}
}}
```''',
    "sql": '''```sql
CREATE TABLE IF NOT EXISTS {table_name} (
    id          BIGSERIAL PRIMARY KEY,
    topic       TEXT NOT NULL,
    variant     INTEGER NOT NULL DEFAULT {variant},
    payload     JSONB NOT NULL,
    created_at  TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_{table_name}_topic ON {table_name} (topic);

EXPLAIN ANALYZE
SELECT id, topic, payload FROM {table_name}
WHERE topic = '{topic}' ORDER BY created_at DESC LIMIT 50;
```''',
    "html_css": '''```html
<section class="{service_name}" data-topic="{topic}">
  <h2>{docstring}</h2>
  <p>Variant {variant}</p>
</section>
<style>.{service_name} {{ padding: 1rem; }}</style>
```''',
    "bash": '''```bash
#!/usr/bin/env bash
set -euo pipefail
TOPIC="{topic}"
VARIANT={variant}
kubectl rollout status deployment/{service_name}
```''',
    "powershell": '''```powershell
$Topic = "{topic}"
$Variant = {variant}
Get-Service -Name "{service_name}" | Restart-Service -Force
```''',
    "dockerfile": '''```dockerfile
FROM python:3.12-slim
WORKDIR /app
ENV TOPIC={topic} VARIANT={variant}
CMD ["python", "-m", "app.main"]
```''',
    "yaml": '''```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {service_name}
spec:
  replicas: {variant}
  template:
    spec:
      containers:
        - name: app
          image: coltex/{service_name}:{variant}
          env:
            - name: TOPIC
              value: "{topic}"
```''',
    "hcl": '''```hcl
resource "aws_instance" "{service_name}" {{
  instance_type = "t3.medium"
  tags = {{ Topic = "{topic}", Variant = "{variant}" }}
}}
```''',
    "nginx": '''```nginx
upstream {service_name} {{ server 127.0.0.1:8080; }}
server {{
    listen 80;
    location /{topic}/ {{ proxy_pass http://{service_name}; }}
}}
```''',
}

DEFAULT_CODE_LANGS = ("python", "typescript", "sql", "yaml")
