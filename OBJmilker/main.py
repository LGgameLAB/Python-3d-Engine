from pywavefront import Wavefront
import pickle

heart = Wavefront("OBJmilker/heart.obj", create_materials=True, collect_faces=True)

def desmosFormat():
    x,y,z = [],[],[]
    for v in heart.vertices:
        x.append(v[0])
        y.append(v[1])
        z.append(v[2])

    formatFaces = []
    for c in heart.parser.mesh.faces:
        formatFaces.append(f"polygon(l[{c[0]+1}],l[{c[1]+1}],l[{c[2]+1}])")
    return x, y, x, formatFaces

def saveMesh(wf, out="out.p"):
    data = {'v': wf.vertices, 'f': wf.parser.mesh.faces}
    pickle.dump(data, open(out, "wb"))

def writeMesh(wf, out="out.txt"):
    with open(out, "w") as o:
        o.write(str(heart.vertices) + "\n")
        o.write(str(heart.parser.mesh.faces))

saveMesh(heart)