from pypdf import PdfReader
import ollama as ol

def strip(filename):
    text = ""
    chunked = []
    p = ""
    joined = ""
    reader = PdfReader(filename)
    for page in reader.pages:
        text += page.extract_text() + "\n"
    readtext = text.split("\xa0")
    x = " ".join(readtext)
    chunked_text = x.split('.\n')
    for x in chunked_text:
        chunked += [p]
        p = ""
        for y in x:
            p += y.replace("\n", " ")
    return chunked
embed = []
prompts = strip("1540157347-HarlanEllison-IHaveNoMouthandIMustScream.pdf")
for d in prompts:
    embed += [ol.embeddings(model='nomic-embed-text', prompt=d)]
embeds = open("striped text", "a")
embed.append(embeds)