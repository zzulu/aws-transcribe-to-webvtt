import os
import json


def formatted_time(seconds: float):
    t = [0, 0, 0]
    for index in range(3):
        seconds, r = seconds // 60, seconds % 60
        t[2-index] = f'{int(r):02d}' if index else f'{r:06.3f}'
    return ':'.join(t)


def main():
    with open('input/input.json', 'r') as input_file, open('output/output.vtt', 'w') as output_file:
        output_file.write(f'WEBVTT{os.linesep*2}')

        data = json.load(input_file)
        sentence, start_time, end_time = [], None, None

        for item in data.get('results').get('items'):
            if item.get('type') == 'pronunciation':
                if not start_time:
                    start_time = float(item.get('start_time'))
                end_time = float(item.get('end_time'))
                sentence.append(item.get('alternatives')[0].get('content'))

            elif item.get('type') == 'punctuation':
                sentence[-1] += item.get('alternatives')[0].get('content')
                output_file.write(f'{formatted_time(start_time)} --> {formatted_time(end_time)}{os.linesep}')
                output_file.write(f"{' '.join(sentence)}{os.linesep*2}")
                sentence, start_time, end_time = [], None, None


if __name__ == '__main__':
    main()
