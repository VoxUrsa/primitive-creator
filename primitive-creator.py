# Here we will attempt best practics in merging all previous scripts written to unify functionality
# The attempt is to create a tool that will allow us to create any primitive with defined paramters 

import maya.cmds as cmds

class MR_Window(object):
        
    # constructor
    def __init__(self):
        
        # "self" initial paramaters    
        self.window = "MR_Window"
        self.title = "Primitive Creator"
        self.size = (400, 400)
        self.cubeCreator = 'Cube Creator'
        self.sphereCreator = 'Sphere Creator'           
        # Enforce uniqueness of tool window
        if cmds.window(self.window, exists = True):
            cmds.deleteUI(self.window, window=True)
            
        # Create new window using paramaters set in "self"
        self.window = cmds.window(self.window, title=self.title, widthHeight=self.size)
        
        cmds.columnLayout(adjustableColumn = True)
        
        cmds.text(self.title)
        cmds.separator(height=40)

        cmds.text(self.cubeCreator)
        cmds.separator(height=20)
        
        self.cubeName = cmds.textFieldGrp(label= 'Cube Name: ')
        self.cubeSize = cmds.floatFieldGrp( numberOfFields=3, label='Size: ', value1=1, value2=1, value3=1)
        self.cubeSubdivs = cmds.intSliderGrp(field=True, label='Sub Divs', minValue=1, maxValue=32, value=1)
        
        self.cubeCreateBtn = cmds.button(label = 'Create Cube', command=self.createCube)


# We are attempting to assign hotkeys to trigger this event but we are not doing a good job of it. Will research in depth.
#        cmds.nameCommand('triggerHotkeyEvent', annotation='Select Circle Tool', command='python("self.createCube")')
#        cmds.hotkey( keyShortcut='j', name='triggerHotkeyEvent')


        cmds.separator(height=20)
        cmds.text(self.sphereCreator)
        cmds.separator(height=20)
        self.sphereName = cmds.textFieldGrp(label= 'Sphere Name: ')
        self.sphereRadius = cmds.floatFieldGrp( numberOfFields=1, label='Radius: ', value1=1)
        self.sphereSubdivs = cmds.intSliderGrp(field=True, label='Sub Divs', minValue=4, maxValue=32, value=1)
        self.sphereCreateBtn = cmds.button(label = 'Create Sphere', command=self.createSphere)




        # Display new window
        cmds.showWindow()
        
    def createCube(self, *args):
        
        name = cmds.textFieldGrp(self.cubeName, query=True, text=True)
        
        width = cmds.floatFieldGrp(self.cubeSize, query=True, value1=True)
        height = cmds.floatFieldGrp(self.cubeSize, query=True, value2=True)
        depth = cmds.floatFieldGrp(self.cubeSize, query=True, value3=True)
        
        subdivs = cmds.intSliderGrp(self.cubeSubdivs, query=True, value=True)
        
        cmds.polyCube(name=name, width=width, height=height, depth=depth, subdivisionsWidth=subdivs, subdivisionsHeight=subdivs, subdivisionsDepth=subdivs)
     
        #Human readable output for testing and verification. All attributes will print to console.
        print('Name: ' + name + '\n' + 'Width: ' + str(width) + '\n' + 'Height: ' + str(height) + '\n' + 'Depth: ' + str(depth) + '\n' + 'Subdivisions: ' + str(subdivs))
        
    def createSphere(self, *args):
        
        name = cmds.textFieldGrp(self.sphereName, query=True, text=True)
        
        radius = cmds.floatFieldGrp(self.sphereRadius, query=True, value1=True)
        
        subdivs = cmds.intSliderGrp(self.sphereSubdivs, query=True, value=True)
        
        cmds.polySphere(name=name, radius=radius, subdivisionsX=subdivs, subdivisionsY=subdivs)
     
        #Human readable output for testing and verification. All attributes will print to console.
        print('Name: ' + name + '\n' + 'Radius: ' + str(radius) + '\n' + 'Subdivisions: ' + str(subdivs))
    
# Create an instance of the window                                   
myWindow = MR_Window()