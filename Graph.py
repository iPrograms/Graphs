class Vertex:

    def __init__ ( self, name, parent, color ):
            self.name = name
            self.parent=parent
            self.color=color

    def setColor( self, color ):
            self.color = color

    def setParent( self, parent ):
            self.parent = parent

    def printName( self ):
            print " " , self.name, " "

    def getName( self ):
            return self.name 

    def getColor( self ):
            return self.color
       
class Graph:

    def __init__( self ):
        self.vertices=[]
        self.matrix = [[]]
        
    def addVertices(self, vertice ):
        self.vertices.append( vertice )
        print "vertice", vertice.getName() , " added "

    def generateVertices( self, size ):
        for index in range( size ):
            v = Vertex( index, " ", "white" )
            self.addVertices( v )
        return self.vertices

    def printVertices( self ):
        for i in range( len( self.vertices )):
            print " ( " , self.vertices[ i ].getName() , " )" 

    def generateMatrix( self ):
        self.matrix = [ [ 0 for i in range( len ( self.vertices ) ) ] for x in range( len( self.vertices)) ]
        return self.matrix
    
    def addPath( self, s, d ):
        self.matrix[ s ][ d ] = 1
        
    def printMatrix( self ):
        print self.matrix
        
    def printPath(self):
        print
        print "Paths: "
        for i in range( len(self.matrix)):
             for j in range( len(self.matrix)):
                 if self.matrix[i][j] == 1:
                     print "(",i,"->",j,")",
                     
    def adjacentEdges( self, vertix ):
        neighbors =[]
        for n in range( len( self.matrix ) ):
            if matrix[vertix][n] == 1:
                neighbors.append(self.vertices[n])
        return neighbors
                    
    def DFS(self, matrix, vertix):
       
        self.vertices[vertix].setColor('gray')     
       
       
                       
graph =   Graph()
vertices = graph.generateVertices( 10 )
graph.printVertices()
matrix =  graph.generateMatrix()

graph.addPath(2,3)
graph.addPath(1,6)
graph.addPath(3,6)
graph.addPath(2,8)
graph.addPath(8,5)
graph.addPath(3,1)
graph.addPath(3,2)
graph.addPath(2,4)
graph.addPath(2,1)
graph.addPath(8,2)
graph.addPath(3,4)
graph.addPath(3,5)
graph.addPath(6,4)
graph.addPath(6,5)
graph.addPath(7,4)
graph.addPath(7,2)
graph.addPath(8,4)
graph.addPath(9,2)

graph.printPath()
graph.DFS( matrix, 0)


                                                                                      



