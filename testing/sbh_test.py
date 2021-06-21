import requests
import urllib
import requests, zipfile, io

eval_url = "http://127.0.0.1:5000/evaluate"
run_url = "http://127.0.0.1:5000/run"

data = """{"complete_sbol": "testing", 
            "shallow_sbol": "", 
            "genbank": "", 
            "top_level": "", 
            "size": 39, 
            "type": "Component", 
            "instanceUrl": ""}"""

def test():
    eval_response = requests.post(eval_url, data=data)
    run_response = requests.post(run_url, data=data)
    print(eval_response.text)
    print(run_response.text)
    #z = zipfile.ZipFile(io.BytesIO(run_response.content))
    #z.extractall("out")


if __name__ == "__main__": test()