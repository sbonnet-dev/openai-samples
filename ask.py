import sys, getopt
import openai

def get_response(text):
   openai.api_key = "YOUR KEY"
   model = "text-davinci-002"
   prompt = text

   response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=1024,
        top_p=1,
        temperature=0.7,
   )

   return response["choices"][0]["text"]

def main(argv):
   question = ''
   opts, args = getopt.getopt(argv,"hq:",["question="])
   for opt, arg in opts:
      if opt == '-h':
         print ('ask.py -q <question>')
         sys.exit()
      elif opt in ("-q", "--question"):
         question = arg
      print ('Question: ', question)
      print ('Response: ', get_response(question))
  
if __name__ == "__main__":
   main(sys.argv[1:])
