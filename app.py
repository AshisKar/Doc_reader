from flask import Flask, request
import math

app = Flask(__name__)


@app.route('/', defaults={'file_name': None})
@app.route('/<file_name>/')
def read_text(file_name):
    lines_count = 0
    array_of_lines = []
    if not file_name:
        file_name = 'file1.txt'

    start_line = int(request.args.get('start', 0))
    # hardcoded line end for now
    end_line = int(request.args.get('end', 1000))

    with open(file_name, 'r') as reader:
        for line in reader.readlines():
            lines_count += 1
            if start_line < lines_count <= end_line:
                array_of_lines.append(line)

    return {
        "file_read": file_name,
        "number_of_lines_read": len(array_of_lines),
        "lines": array_of_lines
    }


if __name__ == '__main__':
    app.run()
