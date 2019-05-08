import testmodel
def get_text(str):
  #str=input("Enter the text to be summarized")
  p=str.find('.')
  headline=str[:p]
  story=str[p+1:]
  story=[story]
  headline=[headline]
  print(story)
  print(headline)
  at,acs,cs=testmodel.processinput(story,headline)
  return at,acs,cs
