inputFileName = input("Minkäniminen tiedosto luodaan?: ")
inputText = input("Mitä kirjoitetaan tiedostoon?: ")
createFile = open(inputFileName, "x")
createFile.write(inputText)

print("Luotiin tiedosto ", inputFileName, " ja siihen tallennettiin teksti: ", inputText)