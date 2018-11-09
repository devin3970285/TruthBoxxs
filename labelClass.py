
import cv2

class Label:


	def __init__(self, img, pos, str):
		## x,y
		self.img = img
		self.str = str

		self.scale = 1
		self.thickness = 2
		self.color = (0,0,255)
		self.margin = 5
		self.font = cv2.FONT_HERSHEY_SIMPLEX

		### [[w,h],baseline]
		self.size = self.get_size()
		self.pos = [pos[0], pos[1] + self.size[0][1] + self.margin]

	def draw(self):
		cv2.putText(self.img,self.str,(self.pos[0],self.pos[1]), self.font, self.scale ,self.color,self.thickness)


	def change_str(self,str):
		self.str = str
		draw()

	def get_size(self):

		return cv2.getTextSize(self.str, self.font, self.scale, self.thickness);

	def get_range(self):

		self.size

		return [self.pos[0],self.pos[1], self.pos[0]+self.size[0][1], self.pos[1] + self.size[0][1]]
