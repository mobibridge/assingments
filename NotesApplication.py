class NotesApplication(object):
	def __init__(self, author):
		self.author = author
		self.notes = []
	
	def create(self, note_content):
		self.notes.append(note_content)
		
	def list(self):
		for index, mynote_id in enumerate(range(len(self.notes))):
		  print("Note ID: {}".format(mynote_id)); #how to add vertical spaciing
		  print("\n");
		  print("By Author {}".format(self.author));
		  #return note_id;
		  
    def get(self, not):		  
		return self.notes[note_id];

	def search(self, search_text):
		print("Showing results for search {}".format(search_text));
		for word in self.notes:
			location = word.find(search_text,0,len(word))
			if location >= 0:
				print("Note ID: {}".format(note_id)); #how to add vertical spaciing
		  		print("\n");
		  		print("By Author {}".format(self.author));

	def edit(self, note_id, new_content):
		self.note_id = new_content; 		  		
		print(self.note_id);

notes = NotesApplication("Michael");