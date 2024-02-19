import re     

regexp = r'\d'
    
def sanitize_file(source, output):
    with open(source, 'r') as src_file:
        with open(output, 'w') as output_file:    
            text = src_file.read()
            sanitized_text = re.sub(regexp, '', text)
            output_file.write(sanitized_text)