import indicoio
import random


class CodeNamesBot(object):
	
	def __init__(self):
		# sensitivity level for hwo related two words are
		self.relevance_sensitivity = .37

		# codenames workds
		self.all_words = ["account","achiever","acoustics","act","action","activity","actor","addition","adjustment","advertisement","advice","aftermath","afternoon","afterthought","agreement","air","airplane","airport","alarm","amount","amusement","anger","angle","animal","answer","ant","ants","apparatus","apparel","apple","apples","appliance","approval","arch","argument","arithmetic","arm","army","art","attack","attempt","attention","attraction","aunt","authority","babies","baby","back","badge","bag","bait","balance","ball","balloon","balls","banana","band","base","baseball","basin","basket","basketball","bat","bath","battle","bead","beam","bean","bear","bears","beast","bed","bedroom","beds","bee","beef","beetle","beggar","beginner","behavior","belief","believe","bell","bells","berry","bike","bikes","bird","birds","birth","birthday","bit","bite","blade","blood","blow","board","boat","boats","body","bomb","bone","book","books","boot","border","bottle","boundary","box","boy","boys","brain","brake","branch","brass","bread","breakfast","breath","brick","bridge","brother","brothers","brush","bubble","bucket","building","bulb","bun","burn","burst","bushes","business","butter","button","cabbage","cable","cactus","cake","cakes","calculator","calendar","camera","camp","can","cannon","canvas","cap","caption","car","card","care","carpenter","carriage","cars","cart","cast","cat","cats","cattle","cause","cave","celery","cellar","cemetery","cent","chain","chair","chairs","chalk","chance","change","channel","cheese","cherries","cherry","chess","chicken","chickens","children","chin","church","circle","clam","class","clock","clocks","cloth","cloud","clouds","clover","club","coach","coal","coast","coat","cobweb","coil","collar","color","comb","comfort","committee","company","comparison","competition","condition","connection","control","cook","copper","copy","cord","cork","corn","cough","country","cover","cow","cows","crack","cracker","crate","crayon","cream","creator","creature","credit","crib","crime","crook","crow","crowd","crown","crush","cry","cub","cup","current","curtain","curve","cushion","dad","daughter","day","death","debt","decision","deer","degree","design","desire","desk","destruction","detail","development","digestion","dime","dinner","dinosaurs","direction","dirt","discovery","discussion","disease","disgust","distance","distribution","division","dock","doctor","dog","dogs","doll","dolls","donkey","door","downtown","drain","drawer","dress","drink","driving","drop","drug","drum","duck","ducks","dust","ear","earth","earthquake","edge","education","effect","egg","eggnog","eggs","elbow","end","engine","error","event","example","exchange","existence","expansion","experience","expert","eye","eyes","face","fact","fairies","fall","family","fan","fang","farm","farmer","father","father","faucet","fear","feast","feather","feeling","feet","fiction","field","fifth","fight","finger","finger","fire","fireman","fish","flag","flame","flavor","flesh","flight","flock","floor","flower","flowers","fly","fog","fold","food","foot","force","fork","form","fowl","frame","friction","friend","friends","frog","frogs","front","fruit","fuel","furniture","alley","game","garden","gate","geese","ghost","giants","giraffe","girl","girls","glass","glove","glue","goat","gold","goldfish","good-bye","goose","government","governor","grade","grain","grandfather","grandmother","grape","grass","grip","ground","group","growth","guide","guitar","gun","hair","haircut","hall","hammer","hand","hands","harbor","harmony","hat","hate","head","health","hearing","heart","heat","help","hen","hill","history","hobbies","hole","holiday","home","honey","hook","hope","horn","horse","horses","hose","hospital","hot","hour","house","houses","humor","hydrant","ice","icicle","idea","impulse","income","increase","industry","ink","insect","instrument","insurance","interest","invention","iron","island","jail","jam","jar","jeans","jelly","jellyfish","jewel","join","joke","journey","judge","juice","jump","kettle","key","kick","kiss","kite","kitten","kittens","kitty","knee","knife","knot","knowledge","laborer","lace","ladybug","lake","lamp","land","language","laugh","lawyer","lead","leaf","learning","leather","leg","legs","letter","letters","lettuce","level","library","lift","light","limit","line","linen","lip","liquid","list","lizards","loaf","lock","locket","look","loss","love","low","lumber","lunch","lunchroom","machine","magic","maid","mailbox","man","manager","map","marble","mark","market","mask","mass","match","meal","measure","meat","meeting","memory","men","metal","mice","middle","milk","mind","mine","minister","mint","minute","mist","mitten","mom","money","monkey","month","moon","morning","mother","motion","mountain","mouth","move","muscle","music","nail","name","nation","neck","need","needle","nerve","nest","net","news","night","noise","north","nose","note","notebook","number","nut","oatmeal","observation","ocean","offer","office","oil","operation","opinion","orange","oranges","order","organization","ornament","oven","owl","owner","page","pail","pain","paint","pan","pancake","paper","parcel","parent","park","part","partner","party","passenger","paste","patch","payment","peace","pear","pen","pencil","person","pest","pet","pets","pickle","picture","pie","pies","pig","pigs","pin","pipe","pizzas","place","plane","planes","plant","plantation","plants","plastic","plate","play","playground","pleasure","plot","plough","pocket","point","poison","police","polish","pollution","popcorn","porter","position","pot","potato","powder","power","price","print","prison","process","produce","profit","property","prose","protest","pull","pump","punishment","purpose","push","quarter","quartz","queen","question","quicksand","quiet","quill","quilt","quince","quiver","rabbit","rabbits","rail","railway","rain","rainstorm","rake","range","rat","rate","ray","reaction","reading","reason","receipt","recess","record","regret","relation","religion","representative","request","respect","rest","reward","rhythm","rice","riddle","rifle","ring","rings","river","road","robin","rock","rod","roll","roof","room","root","rose","route","rub","rule","run","sack","sail","salt","sand","scale","scarecrow","scarf","scene","scent","school","science","scissors","screw","sea","seashore","seat","secretary","seed","selection","self","sense","servant","shade","shake","shame","shape","sheep","sheet","shelf","ship","shirt","shock","shoe","shoes","shop","show","side","sidewalk","sign","silk","silver","sink","sister","sisters","size","skate","skin","skirt","sky","slave","sleep","sleet","slip","slope","smash","smell","smile","smoke","snail","snails","snake","snakes","sneeze","snow","soap","society","sock","soda","sofa","son","song","songs","sort","sound","soup","space","spade","spark","spiders","sponge","spoon","spot","spring","spy","square","squirrel","stage","stamp","star","start","statement","station","steam","steel","stem","step","stew","stick","sticks","stitch","stocking","stomach","stone","stop","store","story","stove","stranger","straw","stream","street","stretch","string","structure","substance","sugar","suggestion","suit","summer","sun","support","surprise","sweater","swim","swing","system","table","tail","talk","tank","taste","tax","teaching","team","teeth","temper","tendency","tent","territory","test","texture","theory","thing","things","thought","thread","thrill","throat","throne","thumb","thunder","ticket","tiger","time","tin","title","toad","toe","toes","tomatoes","tongue","tooth","toothbrush","toothpaste","top","touch","town","toy","toys","trade","trail","train","trains","tramp","transport","tray","treatment","tree","trees","trick","trip","trouble","trousers","truck","trucks","tub","turkey","turn","twig","twist","umbrella","uncle","underwear","unit","use","vacation","value","van","vase","vegetable","veil","vein","verse","vessel","vest","view","visitor","voice","volcano","volleyball","voyage","walk","wall","war","wash","waste","watch","water","wave","waves","wax","way","wealth","weather","week","weight","wheel","whip","whistle","wilderness","wind","window","wine","wing","winter","wire","wish","woman","women","wood","wool","word","work","worm","wound","wren","wrench","wrist","writer","writing","yak","yam","yard","yarn","year","yoke","zebra","zephyr","zinc","zipper","zoo"]
		self.make_word_set()
		self.print_word_set()
		self.group_seeds()
		while True:
			self.get_clue()

	def make_word_set(self):
		#Grabs 25 random words for the round
		self.words = {}
		while len(self.words) < 25:
			self.words[random.choice(self.all_words)] = 0
		self.words = self.words.keys()

	def print_word_set(self):
		#prints the list of words
		for i in range(5):
			word_list = ""
			for j in range(5):
				word_list = word_list + " " + self.words[i*5 +j]
			print word_list

	def get_clue(self):
		# Gets clue input from the user and returns the program's guesses
		#Get clue and num
		clue, num = raw_input("What is your clue?").split(" ")
		num = int(num)
		# Checks how relevant the words are to the clue
		outcome = indicoio.relevance([clue], self.words)[0]
		# Sort the relevance list
		sort_outcome = sorted(outcome)
		for i in range(num):
			# Get the index of the relevant word 
			index = outcome.index(sort_outcome[-1*i - 1])
			print self.words[index]
			print sort_outcome[-1*i - 1]
		
	def group_seeds(self):
		# To help with clue giving, group words that might potentially be related
		groups = {}
		# Compute the relevance of all words to each other 
		word_matrices = indicoio.relevance(self.words, self.words)
		for i in range(len(self.words)):
			for j in range(i+1, len(self.words)):
				#If two words relevance are over the relevance_sensitivity, store them
				if word_matrices[i][j] > self.relevance_sensitivity:
					groups.setdefault(self.words[i],[]).append(self.words[j])
					groups.setdefault(self.words[j],[]).append(self.words[i])
		print groups

cnb = CodeNamesBot()

# # single example
# print indicoio.relevance("Renowned soccer legend Pele will be visiting...", ["team sports", "royalty"])

# 