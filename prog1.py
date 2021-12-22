class Graph:
    def __init__(self, adjac_lst):
        self.adjac_lst = adjac_lst

    def get_neighbor(self, v):
        return self.adjac_lst[v]

    def h(self, n):
        H = {
            'A': 1,
            'B': 1,
            'C': 1,
            'D': 1
        }
        return H[n]

    def a_star(self,start,stop):
        open_lst= set(start)
        closed_lst= set()
        dist ={}
        prenode={}
        

        dist[start]=0 #distance form the start to start is 0.
        prenode[start]= start
        while len(open_lst)>0:
            n= None
            for v in open_lst:
                if n==None or dist[v]+self.h(v)<=dist[n]:
                    n=v
            if(n==None):
                print('Path does not exist')
                return None
            if n == stop:
                reconst_path= []
                while prenode[n] != n :
                    reconst_path.append(n)
                    n = prenode[n]
                reconst_path.append(start)
                reconst_path.reverse()
                print('Path found :{}'.format(reconst_path))
                return #reconst_path

            for(m,weight) in self.get_neighbor(n):
                if m not in open_lst and m not in closed_lst:
                    open_lst.add(m)
                    prenode[m]=n
                    dist[m]= dist[n]+ weight
                else:
                    if dist[m]> dist[n]+weight:
                        dist[m]= dist[n]+weight
                        prenode[m]=n
                        if m in closed_lst:
                            closed_lst.remove(m)
                            open_lst.add (m)
            open_lst.remove(n)
            closed_lst.add(n)
        print('Path does not exist')
        return None

adjac_lst = {
    'A' : [ ('B' , 1), ('C', 3), ('D', 7)],
    'B' : [('D' , 5)],
    'C' : [('D' , 12)]
}

graph1 = Graph(adjac_lst)
graph1.a_star('A', 'D')