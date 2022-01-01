def DrawFrame(Verb_b,typeof,Verb,Verb_s,Verb_ing,Verb_ed):
        if Verb_b == "i":
                print "+------------Χρονική Αντικατάσταση του ρήματος",Verb," στο ",Verb_b,"--------------------+"
                print "                 Present Simple                           Present Continuous"
                print "Kατάφαση>        ",Verb_b,Verb+"                                 ",Verb_b,"am",Verb_ing
                print "Eρώτηση >         Do",Verb_b,Verb+"?                              Am",Verb_b,Verb_ing+"?"
                print "Aρνηση  >        ",Verb_b,"don't",Verb+"                           ",Verb_b+"'m not",Verb_ing
                print ""
                print "                 Past Simple                              Past Continuous"
                print ""
                print "Κατάφαση>        ",Verb_b,Verb_ed+"                                 ",Verb_b,"was",Verb_ing
                print "Ερώτηση >         Did",Verb_b,Verb_ed+"?                             was",Verb_b,Verb_ing+"?"
                print "Άρνηση  >        ",Verb_b,"didn't",Verb_ed+"                          ",Verb_b,"wasn't",Verb_ing
                print ""
                print "                 Used To                                  Be Going To"
                print ""
                print "Κατάφαση>        ",Verb_b," used to ",Verb+"                       ",Verb_b,"going to",Verb
                print "Ερώτηση >         Did ",Verb_b," use to ",Verb+"?","                 ",typeof,Verb_b,"going to",Verb,"?"
                print "Άρνηση  >        ",Verb_b," didn't use to ",Verb+"                       ------------"
                print ""
                print "                 Present Perfect Simple                   Present Perfect Continuous"
                print ""
                print "Κατάφαση>        ",Verb_b,"have",Verb_ed+"                            ",Verb_b+"'ve been",Verb_ing
                print "Ερώτηση >         Have",Verb_b,Verb_ed+"?                            Have",Verb_b,"been",Verb_ing+"?"
                print "Άρνηση  >        ",Verb_b,"haven't",Verb_ed+"                         ",Verb_b,"haven't been",Verb_ing
                print ""
                print "                 Past Perfect Simple                      Future Simple"
                print ""
                print "Κατάφαση>        ",Verb_b,"had",Verb_ed+"                         ",Verb_b,"will",Verb
                print "Ερώτηση >         Had",Verb_b,Verb_ed+"?                         Will",Verb_b,Verb+"?"
                print "Άρνηση  >        ",Verb_b,"hadn't",Verb_ed+"                      ",Verb_b,"won't",Verb
                print ""
                print "                 Future Continuous                        Future Perfect Simple"
                print ""
                print "Κατάφαση>        ",Verb_b,"will be",Verb_ing+"                  ",Verb_b,"will have",Verb_ed
                print "Ερώτηση >         Will",Verb_b,"be",Verb_ing+"?                   Will",Verb_b,"have",Verb_ed+"?"
                print "Άρνηση  >        ",Verb_b,"won't be",Verb_ing+"                  ",Verb_b,"won't have",Verb_ed
                print""
                print "+----------------------------------------------------------------------------------------+"
        if Verb_b =="you":
                print "+------------Χρονική Αντικατάσταση του ρήματος",Verb,"στο",Verb_b,"--------------------+"
                print "                 Present Simple                           Present Continuous"
                print "Kατάφαση>        ",Verb_b,Verb+"                                 ",Verb_b,typeof,Verb_ing
                print "Eρώτηση >         Do",Verb_b,Verb+"?                             ",typeof,Verb_b,Verb_ing+"?"
                print "Aρνηση  >        ",Verb_b,"don't",Verb+"                           ",Verb_b,typeof+"n't",Verb_ing
                print ""
                print "                 Past Simple                              Past Continuous"
                print ""
                print "Κατάφαση>        ",Verb_b,Verb_ed+"                                 ",Verb_b,"were",Verb_ing
                print "Ερώτηση >         Did",Verb_b,Verb_ed+"?                             Were",Verb_b,Verb_ing+"?"
                print "Άρνηση  >        ",Verb_b,"didn't",Verb_ed+"                          ",Verb_b,"weren't",Verb_ing
                print ""
                print "                 Used To                                  Be Going To"
                print ""
                print "Κατάφαση>        ",Verb_b," used to ",Verb+"                       ",Verb_b,"going to",Verb
                print "Ερώτηση >         Did ",Verb_b," use to ",Verb+"?","                 ",typeof,Verb_b,"going to",Verb,"?"
                print "Άρνηση  >        ",Verb_b," didn't use to ",Verb+"                       ------------"
                print ""
                print "                 Present Perfect Simple                   Present Perfect Continuous"
                print ""
                print "Κατάφαση>        ",Verb_b,"have",Verb_ed+"                            ",Verb_b+"'ve been",Verb_ing
                print "Ερώτηση >         Have",Verb_b,Verb_ed+"?                            Have",Verb_b,"been",Verb_ing+"?"
                print "Άρνηση  >        ",Verb_b,"haven't",Verb_ed+"                         ",Verb_b,"haven't been",Verb_ing
                print ""
                print "                 Past Perfect Simple                      Future Simple"
                print ""
                print "Κατάφαση>        ",Verb_b,"had",Verb_ed+"                        ",Verb_b,"will",Verb
                print "Ερώτηση >         Had",Verb_b,Verb_ed+"?                        Will",Verb_b,Verb+"?"
                print "Άρνηση  >        ",Verb_b,"hadn't",Verb_ed+"                     ",Verb_b,"won't",Verb
                print ""
                print "                 Future Continuous                        Future Perfect Simple"
                print ""
                print "Κατάφαση>        ",Verb_b,"will be",Verb_ing+"                   ",Verb_b,"will have",Verb_ed
                print "Ερώτηση >         Will",Verb_b,"be",Verb_ing+"?                   Will",Verb_b,"have",Verb_ed+"?"
                print "Άρνηση  >        ",Verb_b,"won't be",Verb_ing+"                  ",Verb_b,"won't have",Verb_ed
                print "+----------------------------------------------------------------------------------------+"
        if Verb_b == "he" or Verb_b == "she" or Verb_b == "it":
                print "+------------Χρονική Αντικατάσταση του ρήματος",Verb,"στο",Verb_b,"--------------------+"
                print "                 Present Simple                           Present Continuous"
                print "Kατάφαση>        ",Verb_b,Verb_s+"                              ",Verb_b,typeof,Verb_ing
                print "Eρώτηση >         Do",Verb_b,Verb_s+"?                          ",typeof,Verb_b,Verb_ing+"?"
                print "Aρνηση  >        ",Verb_b,"don't",Verb_s+"                        ",Verb_b,typeof+"n't",Verb_ing
                print ""
                print "                 Past Simple                              Past Continuous"
                print ""
                print "Κατάφαση>        ",Verb_b,Verb_ed+"                                 ",Verb_b,"was",Verb_ing
                print "Ερώτηση >         Did",Verb_b,Verb_ed+"?                             Was",Verb_b,Verb_ing+"?"
                print "Άρνηση  >        ",Verb_b,"didn't",Verb_ed+"                          ",Verb_b,"wasn't",Verb_ing
                print ""
                print "                 Used To                                  Be Going To"
                print ""
                print "Κατάφαση>        ",Verb_b," used to ",Verb+"                       ",Verb_b,"going to",Verb
                print "Ερώτηση >         Did ",Verb_b," use to ",Verb+"?","                 ",typeof,Verb_b,"going to",Verb,"?"
                print "Άρνηση  >        ",Verb_b," didn't use to ",Verb+"                       ------------"
                print ""
                print "                 Present Perfect Simple                   Present Perfect Continuous"
                print ""
                print "Κατάφαση>        ",Verb_b,"has",Verb_ed+"                            ",Verb_b+"'s been",Verb_ing
                print "Ερώτηση >         Has",Verb_b,Verb_ed+"?                            Has",Verb_b,"been",Verb_ing+"?"
                print "Άρνηση  >        ",Verb_b,"hasn't",Verb_ed+"                         ",Verb_b,"hasn't been",Verb_ing
                print ""
                print "                 Past Perfect Simple                      Future Simple"
                print ""
                print "Κατάφαση>        ",Verb_b,"had"+Verb_ed,"                        ",Verb_b,"will",Verb
                print "Ερώτηση >         Had",Verb_b,Verb_ed+"?                        Will",Verb_b,Verb+"?"
                print "Άρνηση  >        ",Verb_b,"hadn't",Verb_ed+"                     ",Verb_b,"won't",Verb
                print ""
                print "                 Future Continuous                        Future Perfect Simple"
                print ""
                print "Κατάφαση>        ",Verb_b,"will be",Verb_ing+"                   ",Verb_b,"will have",Verb_ed
                print "Ερώτηση >         Will",Verb_b,"be",Verb_ing+"?                   Will",Verb_b,"have",Verb_ed+"?"
                print "Άρνηση  >        ",Verb_b,"won't be",Verb_ing+"                  ",Verb_b,"won't have",Verb_ed
                print "+----------------------------------------------------------------------------------------+"
        if Verb_b == "we" or Verb_b == "---" or Verb_b == "they":
                print "+------------Χρονική Αντικατάσταση του ρήματος",Verb,"στο",Verb_b,"--------------------+"
                print "                 Present Simple                           Present Continuous"
                print "Kατάφαση>        ",Verb_b,Verb,"                                ",Verb_b,typeof,Verb_ing
                print "Eρώτηση >         Do",Verb_b,Verb+"?                            ",typeof,Verb_b,Verb_ing+"?"
                print "Aρνηση  >        ",Verb_b,"don't",Verb,"                          ",Verb_b,typeof+"n't",Verb_ing
                print ""
                print "                 Past Simple                              Past Continuous"
                print ""
                print "Κατάφαση>        ",Verb_b,Verb_ed,"                                 ",Verb_b,"were",Verb_ing
                print "Ερώτηση >         Did",Verb_b,Verb_ed+"?                             Were",Verb_b,Verb_ing+"?"
                print "Άρνηση  >        ",Verb_b,"didn't",Verb_ed,"                          ",Verb_b,"weren't",Verb_ing
                print ""
                print "                 Used To                                  Be Going To"
                print ""
                print "Κατάφαση>        ",Verb_b," used to ",Verb,"                       ",Verb_b,"going to",Verb
                print "Ερώτηση >         Did ",Verb_b," use to ",Verb+"?","                 ",typeof,Verb_b,"going to",Verb,"?"
                print "Άρνηση  >        ",Verb_b," didn't use to ",Verb,"                       ------------"
                print ""
                print "                 Present Perfect Simple                   Present Perfect Continuous"
                print ""
                print "Κατάφαση>        ",Verb_b,"have",Verb_ed,"                            ",Verb_b+"'ve been",Verb_ing
                print "Ερώτηση >         Have",Verb_b,Verb_ed+"?                            Have",Verb_b,"been",Verb_ing
                print "Άρνηση  >        ",Verb_b,"haven't",Verb_ed,"                         ",Verb_b,"haven't been",Verb_ing
                print ""
                print "                 Past Perfect Simple                      Future Simple"
                print ""
                print "Κατάφαση>        ",Verb_b,"had",Verb_ed,"                        ",Verb_b,"will",Verb
                print "Ερώτηση >         Had",Verb_b,Verb_ed+"?                        Will",Verb_b,Verb+"?"
                print "Άρνηση  >        ",Verb_b,"hadn't",Verb_ed,"                     ",Verb_b,"won't",Verb
                print ""
                print "                 Future Continuous                        Future Perfect Simple"
                print ""
                print "Κατάφαση>        ",Verb_b,"will be",Verb_ing,"                   ",Verb_b,"will have",Verb_ed
                print "Ερώτηση >         Will",Verb_b,"be",Verb_ing+"?                   Will",Verb_b,"have",Verb_ed+"?"
                print "Άρνηση  >        ",Verb_b,"won't be",Verb_ing,"                  ",Verb_b,"won't have",Verb_ed
                print "+----------------------------------------------------------------------------------------+"
                
#+-----------------------------------------------------------------------------------------------------------------#
print """
                <Χρονική Αντικατάσταση Generator>
                <Απο τον El_Sonador>
                <Έκδοση 1.1>
"""
verb = raw_input("Εισάγετε το ρήμα .. ")
v1 = verb + "-s "
v2 = verb + "-ing "
v3 = verb + "-ed "
b = raw_input("Το οποίο θα κλιθεί ως .. ")
if b == "i" or b == "you" or b == "he" or b == "she" or b == "it":
        Type = "is"
if b == "we" or b == "you" or b == "they": 
        Type = "are"
DrawFrame(b,Type,verb,v1,v2,v3)
