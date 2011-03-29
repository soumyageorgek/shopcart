from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response

def color(request):
  def map_color(list1):
    def adj_matrix(l):
      i = 0
      matrix = []
      for x in l:
        list2 = [0] * len(l)
        for y in x:
          list2[y] = 1
        matrix.append(list2)
      return matrix

    def find_color(mat):
      #return mat
      color = {}
      colors = [1, 2, 3, 4, 5, 6, 7, 8]
      i = 0
      while i < len(mat):
        k = 0
        color[i] = colors[k]
        k += 1
        j = 0
        while j < i:
          if color[i] == color[j] and mat[i][j] == 1:
            color[i] = colors[k]
            k += 1
            j=0
          else:
            j += 1
        i += 1
      return color
        #return {'1':1}
    adjmat = adj_matrix(list1)
    #return adjmat#chg 1
    color = find_color(adjmat)
    #return color#chg2 2
    fin_color = [0]*len(list1)
    for x in color:
      fin_color[x] = color[x]
    return fin_color
  if request.method == 'GET':
    return HttpResponse("ok")
  str1 = request.POST.get('name', '')
  #print str1
  #return HttpResponse(str1) 
   #jsonList = simplejson.dumps(([1, 2, 3]))
   #print jsonlist
   #return HttpResponse(jsonList)
  #str1 = self.request.get('name')
  #fin_color =#chg 2
  #color = str(map_color(eval(str1)))
  #return HttpResponse(color)
  fin_color = map_color(eval(str1))
  return HttpResponse(str(fin_color))

