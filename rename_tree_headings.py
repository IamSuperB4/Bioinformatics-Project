import os
import re

conversion_table = {
    "acutor":"Balaenoptera_acutorostrata - Minke whale",
    "muscul":"Balaenoptera_musculus - Blue whale",
    "indicu":"Bos_indicus - Zebu cattle",
    "mutus|":"Bos_mutus - Wild yak",
    "bactri":"Camelus_bactrianus - Bactrian camel",
    "dromed":"Camelus_dromedarius - Dromedary camel",
    "lupus|":"Canis_lupus_dingo - Austrailan dog",
    "lupus|":"Canis_lupus_familiaris - Domestic dog",
    "canade":"Cervus_canadensis - Elk",
    "elaphu":"Cervus_elaphus - Red deer",
    "ordii|":"Dipodomys_ordii - Ord's kangaroo rat",
    "specta":"Dipodomys_spectabilis - Banner-tailed kangaroo rat",
    "asinus":"Equus_asinus - Donkey",
    "caball":"Equus_caballus - Horse",
    "canade":"Lynx_canadensis - Canada lynx",
    "rufus|":"Lynx_rufus - Bobcat",
    "fascic":"Macaca_fascicularis - Crab-eating macaque",
    "mulatt":"Macaca_mulatta - Rhesus macaque",
    "javani":"Manis_javanica - Sunda pangolin",
    "pentad":"Manis_pentadactyla - Chinese pangolin",
    "flaviv":"Marmota_flaviventris - Yellow-bellied marmot",
    "marmot":"Marmota_marmota - Alpine marmot",
    "ochrog":"Microtus_ochrogaster - Prairie vole",
    "oregon":"Microtus_oregoni - Creeping vole",
    "angust":"Mirounga_angustirostris - Northern elephant seal",
    "leonin":"Mirounga_leonina - Southern elephant seal",
    "ermine":"Mustela_erminea - Stoat (weasel)",
    "putori":"Mustela_putorius - European polecat",
    "caroli":"Mus_caroli - Ryukyu mouse",
    "muscul":"Mus_musculus - House mouse",
    "brandt":"Myotis_brandtii - Brandt's bat",
    "davidi":"Myotis_davidii - David's myotis (bat)",
    "schaui":"Neomonachus_schauinslandi - Hawaiian monk seal",
    "asiaeo":"Neophocaena_asiaeorientalis - Narrow-ridged finless porpoise (small whale)",
    "curzon":"Ochotona_curzoniae - Plateau pika",
    "prince":"Ochotona_princeps - American pika",
    "leo|NC":"Panthera_leo - Lion",
    "pardus":"Panthera_pardus - Leopard",
    "panisc":"Pan_paniscus - Bonobo",
    "troglo":"Pan_troglodytes - Chimpanzee",
    "leucop":"Peromyscus_leucopus - White-footed mouse",
    "manicu":"Peromyscus_maniculatus - Deer Mouse",
    "discol":"Phyllostomus_discolor - Pale spear-nosed bat",
    "hastat":"Phyllostomus_hastatus - Greater spear-nosed bat",
    "bengal":"Prionailurus_bengalensis - Leopard cat",
    "viverr":"Prionailurus_viverrinus - Fishing cat",
    "alecto":"Pteropus_alecto - Black fruit bat",
    "gigant":"Pteropus_giganteus - Greater Indian fruit bat",
    "concol":"Puma_concolor - Cougar",
    "yagoua":"Puma_yagouaroundi - Jaguarundi (wild cat)",
    "norveg":"Rattus_norvegicus - Brown rat",
    "rattus":"Rattus_rattus - Black rat",
    "ferrum":"Rhinolophus_ferrumequinum - Greater horseshoe bat",
    "sinicu":"Rhinolophus_sinicus - Chinese rufous horseshoe bat",
    "bieti|":"Rhinopithecus_bieti - Black-and-white snub-nosed monkey",
    "roxell":"Rhinopithecus_roxellana - Golden snub-nosed monkey",
    "americ":"Ursus_americanus - American black bear",
    "arctos":"Ursus_arctos - Brown bear",
    "lagopu":"Vulpes_lagopus - Arctic fox",
    "vulpes":"Vulpes_vulpes - Red fox"
}

fromDirectory = 'Tree_Files/' # put / at the end of string

listOfFiles = []
 
# iterate over files in  directory
for path, subdirs, files in os.walk(fromDirectory):
    for name in files:
        file_path = os.path.join(path, name) # entire path to file
        
        # check if it is a file
        if os.path.isfile(file_path):
            listOfFiles.append(file_path) # add file to list of files to parse

for direct in listOfFiles:
    file = open(direct)
    fileName = os.path.basename(direct) # pull file name from path

    file_string = file.read();

    for key in conversion_table:

        # only look at the gene we want to research
        if(key in file_string):
            print("Replacing " + key + " with " + conversion_table[key])
            file_string = file_string.replace(key, conversion_table[key])

    file_string = file_string.replace("lcl_", "")

    print("Overwriting file: " + fileName)
    with open(direct, "w") as f:
        f.write(file_string)


