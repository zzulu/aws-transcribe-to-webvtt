# AWS Transcribe to WebVTT


## How to use

- Input file: `input/input.json`
- Output file: `output/output.vtt`

```bash
$ python main.py
```


## Examples

### Example Input (AWS Transcribe Output)

```json
{
  "jobName": "happy-story",
  "accountId": "323249573163",
  "results": {
    "transcripts": [
      {
        "transcript": "안녕하세요. 해피해킹에"
      }
    ],
    "items": [
      {
        "start_time": "2.04",
        "end_time": "2.77",
        "alternatives": [
          {
            "confidence": "1.0",
            "content": "안녕하세요"
          }
        ],
        "type": "pronunciation"
      },
      {
        "alternatives": [
          {
            "confidence": "0.0",
            "content": "."
          }
        ],
        "type": "punctuation"
      },
      {
        "start_time": "2.89",
        "end_time": "3.64",
        "alternatives": [
          {
            "confidence": "0.6768333333333333",
            "content": "해피해킹에"
          }
        ],
        "type": "pronunciation"
      }
    ]
  },
  "status": "COMPLETED"
}
```

### Example Output (WebVTT Format)

```
WEBVTT

00:00:02.040 --> 00:00:02.770
안녕하세요.

00:00:02.890 --> 00:00:04.380
해피해킹에
```

