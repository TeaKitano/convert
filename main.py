import streamlit as st

def output(l):
    html=['<!--CSS（表のデザインの変更コード）-->\n', '<style>\n', '  .table-design{\n', '  overflow: auto;\n', '  width: 100%;\n', '  text-align: center;\n', '  font-size: 12px;\n', '  }\n', '  .table-design table{\n', '  margin: 0px auto;\n', '  border-spacing: 0;\n', '  \n', '  }\n', '  .table-design td{\n', '  white-space: nowrap;\n', '  border-right: 1px solid #999;\n', '  border-bottom: 1px solid #999;\n', '  background: #FFF;\n', '  padding: 5px;\n', '  }\n', '  .table-design th{\n', '  white-space: nowrap;\n', '  border-right: 1px solid #999;\n', '  border-bottom: 1px solid #999;\n', '  background: #f2f2f2;\n', '  position: sticky;\n', '  padding: 0px 10px;\n', '  top: 0;\n', '  left: 0;\n', '  }\n', '  \n', '  .table-design thead th{\n', '  border-top: 1px solid #999;\n', '  border-bottom: 1px solid #000;\n', '  }\n', '  .table-design tbody tr:first-child th{\n', '  border-bottom: 1px solid #000;\n', '  }\n', '  .table-design th:first-child{\n', '  border-left: 1px solid #999;\n', '  border-right: 1px solid #000;\n', '  }\n', '  .table-design td:nth-child(2) {\n', '    font-weight: bold;\n', '  }\n', '  .table-design td:nth-child(5) {\n', '    font-weight: bold;\n', '  }\n', '  .table-design td:nth-child(12) {\n', '    font-weight: bold;\n', '  }\n', '  .table-design th:nth-child(2) {\n', '    border-right: 1px solid #000;\n', '  }\n', '  .table-design th:nth-child(3) {\n', '    border-right: 1px solid #000;\n', '  }\n', '  .table-design th:nth-child(4) {\n', '    border-right: 1px solid #000;\n', '  }\n', '  .table-design th:nth-child(5) {\n', '    border-right: 1px solid #000;\n', '  }\n', '  .table-design th:nth-child(7) {\n', '    border-right: 1px solid #000;\n', '  }\n', '  .table-design th:nth-child(9) {\n', '    border-right: 1px solid #000;\n', '  }\n', '  .table-design th:nth-child(11) {\n', '    border-right: 1px solid #000;\n', '  }\n', '  .table-design td:nth-child(4) {\n', '    border-right: 1px solid #000;\n', '  }\n', '  .table-design td:nth-child(7) {\n', '    border-right: 1px solid #000;\n', '  }\n', '  .table-design td:nth-child(9) {\n', '    border-right: 1px solid #000;\n', '  }\n', '  .table-design td:nth-child(11) {\n', '    border-right: 1px solid #000;\n', '  }\n', '  .table-design tr:first-child th:first-child{\n', '  z-index: 1;\n', '  }\n', '  .table-design tr:nth-child(2) th:first-child{\n', '  z-index: 1;\n', '  }\n', '  .table-design .bold-line{\n', '  border-bottom: 2px solid #000;\n', '  }\n', '</style>\n', '  \n', '<div class="table-design">\n']
    for i in l:
        for j in i:
            html.append(j+"\n")
    html.append("  </tbody>\n")        
    html.append("</table>\n")
    html.append("</table>\n")
    html.append("</div>\n")
    html.append("<!--分析記事-->\n")
    return html

def convert(s):
    ip=list(s.splitlines())
    ip[3]="<th></th>"
    l=[]
    t=[]
    for i in ip:
        t.append(i)
        if "</tr>" in i:
            l.append(t)
            t=[]

    l[0]=[s for s in l[0] if s!="      <th></th>"]
    l[0][4]=l[0][4].replace("<th>",'<th colspan="3">')
    l[0][5]=l[0][5].replace("<th>",'<th colspan="3">')
    l[0][6]=l[0][6].replace("<th>",'<th colspan="2">')
    l[0][7]=l[0][7].replace("<th>",'<th colspan="2">')
    l[0][8]=l[0][8].replace("<th>",'<th colspan="3">')

    l[1]=[s.replace("td","th") for s in l[1]]
    for i in range(2,len(l)):
        l[i][1]=l[i][1].replace("td","th")
    
    l[-2]=[s.replace("<th>",'<th class="bold-line">') for s in l[-2]]
    l[-2]=[s.replace("<td>",'<td class="bold-line">') for s in l[-2]]
    return output(l)


def main():
    st.set_page_config(layout="wide")
    s = st.text_area('入力', '')
    b=st.button("ボタン")
    if b:
        try:
            html=convert(s)
            st.components.v1.html("\n".join(html),height=500)
            st.text_area('出力', "".join(html))
        except:
            st.text("入力が不正です")
if __name__=="__main__":
    main()
