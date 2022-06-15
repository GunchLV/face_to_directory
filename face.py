import face_recognition
import glob
import shutil

# šis pēc zināmās bildes iziet cauri mapei un pasaka vai ir vai nav tā pati seja

# ko meklēs
zinams = face_recognition.load_image_file("D:/Projects/Pyton projects/Face/a.jpg")
zinams_encoding = face_recognition.face_encodings(zinams)[0]

# kur meklēs
nezinams = glob.glob("D:/Projects/Pyton projects/Face/*.jpg")

# uz kurieni pārkopēs atrastos
rezultata_mape = "D:/Projects/Pyton projects/Face/result"

# meklēšanas process
for nezinam in nezinams:
    try:
        nezinams_encoding = face_recognition.face_encodings(face_recognition.load_image_file(nezinam))[0]
        results = face_recognition.compare_faces([zinams_encoding], nezinams_encoding)
        if str(results) == "[True]":
            print(nezinam + " bildē pazina meklēto seju")
            shutil.copy(nezinam, rezultata_mape)
        else:
            print(nezinam + " bildē nevienu nepazīst")
    except IndexError:
        print(nezinam + " bildē neatrada seju")
