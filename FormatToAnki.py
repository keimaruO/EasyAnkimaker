import re

def parse_input(filename):
    data = []
    with open(filename, "r") as f:
        lines = f.readlines()
        for i in range(0, len(lines), 3):
            match_url = re.search(r'https://youtu.be/(.+?)\?t=(\d+)h(\d+)m(\d+)s', lines[i].strip())
            match_time = re.search(r'(\d+) --> (\d+)', lines[i+1].strip())
            text = lines[i+2].strip()
            if match_url and match_time:
                url = match_url.group(1)
                start = match_time.group(1)
                end = match_time.group(2)
                data.append((url, start, end, text))
    return data

def generate_output(data, output_filename):
    with open(output_filename, "w") as f:
        f.write("#separator:tab\n#html:true\n#tags column:6\n")
        for url, start, end, text in data:
            output = f"{text}\tx\t{start}\t{end}\t{url}\t\n"
            f.write(output)

def main():
    data = parse_input("input.txt")
    generate_output(data, "output.txt")

if __name__ == "__main__":
    main()