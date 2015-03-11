
class Vertice:

    'Constructor'
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
            
