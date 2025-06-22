# from flask import Flask, render_template, request
# import time
# import numpy as np

# app = Flask(__name__)

# def brute_force_search(text, pat, case_sensitive=False, as_whole=True):
#     start_time = time.time()
#     if not case_sensitive:
#         text = text.lower()
#         pat = pat.lower()
    
#     found = []
#     m, n = len(pat), len(text)
    
#     for i in range(n):
#         if text[i] == '^':
#             continue
#         if text[i:i + m] == pat:
#             found.append((i, pat))
    
#     end_time = time.time()
#     print(f"Brute Force found: {found}")  # Debugging line
#     return found, end_time - start_time

# def kmp_matcher(s, p, case_sensitive=False, as_whole=True):
#     start_time = time.time()
#     if not case_sensitive:
#         s = s.lower()
#         p = p.lower()
    
#     found = []
#     m, n = len(p), len(s)
#     prefix = prefix_function(p)
#     q = 0
    
#     for i in range(n):
#         while q > 0 and p[q] != s[i]:
#             q = prefix[q - 1]
#         if p[q] == s[i]:
#             q += 1
#         if q == m:
#             found.append((i, p))
#             q = prefix[q - 1]
    
#     end_time = time.time()
#     print(f"KMP found: {found}")  # Debugging line
#     return found, end_time - start_time

# def prefix_function(p):
#     m = len(p)
#     prefix = np.zeros(m, dtype='int')
#     k = 0
#     for q in range(1, m):
#         while k > 0 and p[k] != p[q]:
#             k = prefix[k - 1]
#         if p[k] == p[q]:
#             k += 1
#         prefix[q] = k
#     return prefix.astype('int')

# def load_texts():
#     text = ""
#     for i in range(1, 11):
#         filename = "C:\\Users\\User\\Downloads\\Assignmnet three\\Assignmnet three\\" + f"Research#{i}.txt"
#         try:
#             with open(filename, 'r', encoding='utf-8') as file:
#                 text += "^" + file.read()
#         except FileNotFoundError:
#             print(f"File not found: {filename}")  # Debugging line
#             continue
#     print(f"Loaded text: {text[:100]}...")  # Print the first 100 characters
#     return text


# @app.route('/', methods=['GET', 'POST'])
# def index():
#     results = []
#     time_taken_brute = 0
#     time_taken_kmp = 0
    
#     if request.method == 'POST':
#         search_term = request.form['search_term']
#         case_sensitive = 'case_sensitive' in request.form
#         whole_word = 'whole_word' in request.form
        
#         if not search_term:
#             return render_template('index.html', error="Please enter a search term.")
        
#         text = load_texts()
        
#         if whole_word:
#             search_term = f" {search_term} "  # Adjust for whole word search

#         # Perform searches
#         results_bf, time_taken_brute = brute_force_search(text, search_term, case_sensitive)
#         results_kmp, time_taken_kmp = kmp_matcher(text, search_term, case_sensitive)

#         results = {
#             'Brute Force': results_bf,
#             'KMP': results_kmp
#         }
    
#     return render_template('index.html', results=results, time_taken_brute=time_taken_brute, time_taken_kmp=time_taken_kmp)

# if __name__ == '__main__':
#     app.run(debug=True)





from flask import Flask, render_template, request
import time
import numpy as np

app = Flask(__name__)

def load_texts():
    text = ""
    for i in range(1, 11):
        filename = f"C:\\Users\\User\\Downloads\\Assignmnet three\\Assignmnet three\\Research#{i}.txt"
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                text += "^" + file.read()
        except FileNotFoundError:
            print(f"File not found: {filename}")  # Debugging line
            continue
    print(f"Loaded text: {text[:100]}...")  # Print the first 100 characters
    return text

def Brute_Force(text, pat, case_sensitive=False, as_whole=True):
    start_time = time.time()
    found = 0
    found_whole = 0 
    rownum = 1 
    colnum = 0
    docnum = 0
    m = len(pat)
    n = len(text)

    if not case_sensitive:
        text = text.lower()
        pat = pat.lower()

    results = []  # Store results for display

    for i in range(len(text)):
        c = 0
        if text[i] == '\n':
            rownum += 1
            colnum = 0
        
        if text[i] == '^':
            docnum += 1
            rownum, colnum = 1, 0
            continue

        for j in range(len(pat)):
            c += 1
            if text[i + j] != pat[j]:
                c = 0
                break

        if not as_whole and c == m:
            results.append(f"Doc num: {docnum} | Row num: {rownum} | Col num: {colnum - m + 1} | Pattern FOUND!")
            found += 1

        if i + m > n:
            break

        if as_whole and c == m and ((i == 0 or not text[i - 1].isalnum()) and (i + m >= n or not text[i + len(pat)].isalnum())):
            results.append(f"Doc num: {docnum} | Row num: {rownum} | Col num: {colnum - m + 1} | Whole Pattern FOUND!")
            found_whole += 1

        colnum += 1

    end_time = time.time()
    time_taken = end_time - start_time
    print('found_whole:', found_whole)
    print('found:', found)
    return results, time_taken

def prefix_function(p):
    m = len(p)
    prefix = np.zeros(m, dtype='int')
    prefix[0] = 0
    k = 0

    for q in range(1, m):
        while k > 0 and p[k] != p[q]:
            k = prefix[k - 1]
        if p[k] == p[q]:
            k += 1
        prefix[q] = k
    return prefix.astype('int')

def kmp_matcher(s, p, case_sensitive=False, as_whole=True):
    start_time = time.time()
    if not case_sensitive:
        s = s.lower()
        p = p.lower()
    n = len(s)
    m = len(p)
    prefix = prefix_function(p)
    q = 0
    results, found_whole, found = [], 0, 0
    rownum, colnum, docnum = 1, 0, 0

    for i in range(n):
        if s[i] == '\n':
            rownum += 1
            colnum = 0
        if s[i] == "^":
            docnum += 1
            rownum, colnum = 1, 0
        
        while q > 0 and p[q] != s[i]:
            q = prefix[q - 1]
        if p[q] == s[i]:
            q += 1

        if q == m:
            if as_whole and ((i - m < 0 or not s[i - m].isalnum()) and (i + 1 >= n or not s[i + 1].isalnum())):
                results.append(f"Doc num: {docnum} | Row num: {rownum} | Col num: {colnum - m + 1} | Whole Pattern FOUND!")
                found_whole += 1
            elif not as_whole:
                results.append(f"Doc num: {docnum} | Row num: {rownum} | Col num: {colnum - m + 1} | Pattern FOUND!")
                found += 1
            q = prefix[q - 1]

        colnum += 1

    end_time = time.time()
    time_taken = end_time - start_time
    print('found_whole:', found_whole)
    print('found:', found)
    return results, time_taken

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    text = load_texts()  # Load your texts using your function
    pattern = request.form['pattern']  # Get the pattern from the form
    case_sensitive = request.form.get('case_sensitive', 'false').lower() == 'true'
    as_whole = request.form.get('as_whole', 'true').lower() == 'true'

    # Run the selected algorithm
    if request.form['algorithm'] == 'brute_force':
        results, time_taken = Brute_Force(text, pattern, case_sensitive, as_whole)
    else:
        results, time_taken = kmp_matcher(text, pattern, case_sensitive, as_whole)

    # Return results and time taken to the results.html template
    return render_template('results.html', results=results, time_taken=time_taken)

if __name__ == '__main__':
    app.run(debug=True)











# import numpy as np
# import time
# from flask import Flask, render_template_string, request

# app = Flask(__name__)

# def load_texts():
#     text = ""
#     for i in range(1, 11):
#         filename = "C:\\Users\\User\\Downloads\\Assignmnet three\\Assignmnet three\\" + f"Research#{i}.txt"
#         try:
#             with open(filename, 'r', encoding='utf-8') as file:
#                 text += "^" + file.read()
#         except FileNotFoundError:
#             print(f"File not found: {filename}")  # Debugging line
#             continue
#     print(f"Loaded text: {text[:100]}...")  # Print the first 100 characters
#     return text

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     results = {
#         'kmp_results': [],
#         'brute_results': []
#     }
    
#     if request.method == 'POST':
#         pattern = request.form.get('pattern')  # Get the search pattern from the form
#         if pattern:  # Ensure that the pattern is not empty
#             # Load text from files
#             text = load_texts()

#             # Call both matching functions
#             results['kmp_results'] = kmp_matcher(text, pattern, case_sensitive=False, as_whole=True)
#             results['brute_results'] = brute_force(text, pattern, case_sensitive=False, as_substr=True)

#     return render_template_string("""
#     <h1>Pattern Matching</h1>
#     <form method="POST">
#         <input type="text" name="pattern" placeholder="Enter pattern to search" required>
#         <input type="submit" value="Search">
#     </form>
    
#     <h2>KMP Matcher Results</h2>
#     <ul>
#         {% for result in results.kmp_results %}
#             <li>{{ result }}</li>
#         {% endfor %}
#     </ul>
    
#     <h2>Brute Force Results</h2>
#     <ul>
#         {% for result in results.brute_results %}
#             <li>{{ result }}</li>
#         {% endfor %}
#     </ul>
#     """, results=results)

# def kmp_matcher(s, p, case_sensitive=False, as_whole=True):
#     results = []
#     start_time = time.time()
    
#     if not case_sensitive:
#         s = s.lower()
#         p = p.lower()
    
#     n = len(s)
#     m = len(p)
#     prefix = prefix_function(p)
#     q = 0
#     rownum, colnum, docnum = 1, 0, 0
    
#     for i in range(n):
#         if s[i] == '\n':
#             rownum += 1
#             colnum = 0
#         if s[i] == "^":
#             docnum += 1
#             rownum, colnum = 1, 0
        
#         while q > 0 and p[q] != s[i]:
#             q = prefix[q - 1]
        
#         if p[q] == s[i]:
#             q += 1
            
#         if q == m:
#             if as_whole and ((i - m < 0 or not s[i - m].isalnum()) and (i + 1 >= n or not s[i + 1].isalnum())):
#                 result_str = f"Doc num: {docnum} | Row num: {rownum} | Col num: {colnum - m + 1} | Pattern FOUND!"
#                 results.append(result_str)
#             elif not as_whole:
#                 result_str = f"Doc num: {docnum} | Row num: {rownum} | Col num: {colnum - m + 1} | Pattern FOUND!"
#                 results.append(result_str)

#             q = prefix[q - 1]
#         colnum += 1

#     end_time = time.time()
#     print('KMP Results:', results)
#     return results

# def prefix_function(p):
#     m = len(p)
#     prefix = np.zeros(m, dtype='int')
#     prefix[0] = 0
#     k = 0
#     for q in range(1, m):
#         while k > 0 and p[k] != p[q]:
#             k = prefix[k - 1]
#         if p[k] == p[q]:
#             k += 1
#         prefix[q] = k
#     return prefix.astype('int')

# def brute_force(text, pat, case_sensitive=False, as_substr=True):
#     results = []
#     start_time = time.time()
#     rownum = 1
#     colnum = 0
#     docnum = 0
#     m = len(pat)
#     n = len(text)
    
#     if not case_sensitive:
#         text = text.lower()
#         pat = pat.lower()
        
#     for i in range(n):
#         if text[i] == '\n':
#             rownum += 1
#             colnum = 0
#         if text[i] == '^':
#             docnum += 1
#             rownum, colnum = 1, 0
#             continue
        
#         c = 0
#         for j in range(m):
#             if i + j >= n or text[i + j] != pat[j]:
#                 break
#             c += 1
            
#         if as_substr and c == m:
#             result_str = f"Doc num: {docnum} | Row num: {rownum} | Col num: {colnum} | Pattern FOUND!"
#             results.append(result_str)
            
#         if not as_substr and c == m and ((i == 0 or not text[i - 1].isalnum()) and (i + m >= n or not text[i + len(pat)].isalnum())):
#             result_str = f"Doc num: {docnum} | Row num: {rownum} | Col num: {colnum} | Pattern FOUND!"
#             results.append(result_str)
            
#         colnum += 1

#     end_time = time.time()
#     print('Brute Force Results:', results)
#     return results

# # Run the Flask app
# if __name__ == '__main__':
#     app.run(debug=True)
