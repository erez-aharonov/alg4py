import streamlit as st
import streamlit.components.v1 as components
from notebooks import cst_utils


file_path = '/mnt/hgfs/dev/open_source_projects/alkh/notebooks/play.py'
file_lines = open(file_path).readlines()
file_content = "".join(file_lines)

call_graph_manager = cst_utils.CallGraphManager(file_path)

prism_twilight_min_css_file_path = "./notebooks/prism-twilight.min.css"
prism_twilight_min_css_string = open(prism_twilight_min_css_file_path).read()

line_number = st.sidebar.number_input('line number', min_value=1, max_value=len(file_lines))
variable_name = cst_utils.get_variable_name(file_lines[int(line_number) - 1])
if variable_name is None:
    variable_name = "None"
    lines_numbers_string = line_number
else:
    lines_numbers_list = call_graph_manager.get_variable_affecting_lines(variable_name)
    lines_numbers_string = ",".join(map(str, lines_numbers_list))
    print(lines_numbers_string)

st.sidebar.text(f"variable name: {variable_name}")


html = f"""
<!DOCTYPE html>
<html>
<head>
    <style>{prism_twilight_min_css_string}</style>
	<link href="https://cdn.jsdelivr.net/npm/prismjs@1.28.0/plugins/line-numbers/prism-line-numbers.min.css" rel="stylesheet" />
	<link href="https://cdn.jsdelivr.net/npm/prismjs@1.28.0/plugins/line-highlight/prism-line-highlight.min.css" rel="stylesheet" />		
</head>
<body class="line-numbers"> 
	<header data-plugin-header="line-highlight"></header>
	<pre class="language-python" data-line="{lines_numbers_string}"><code>{file_content}</code></pre>
	<script src="https://cdn.jsdelivr.net/npm/prismjs@1.28.0/prism.min.js"></script>
	<script src="https://cdn.jsdelivr.net/npm/prismjs@1.28.0/plugins/autoloader/prism-autoloader.min.js"></script>
	<script src="https://cdn.jsdelivr.net/npm/prismjs@1.28.0/plugins/line-numbers/prism-line-numbers.min.js"></script>		
	<script src="https://cdn.jsdelivr.net/npm/prismjs@1.28.0/plugins/line-highlight/prism-line-highlight.min.js"></script>
</body>
</html>
"""

components.html(html, height=600, scrolling=True)
