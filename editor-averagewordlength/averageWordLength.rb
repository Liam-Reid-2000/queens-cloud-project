module AverageWordLengthMethods

	def split_to_words(text)
	   return text.split(" ")
	end


	def get_average_word_length(words)
		total = 0
		count = 0
		words.each { |word|
			total = total + word.length
			count = count + 1
		}
		if (total == 0 || count == 0)
			return -1 # -1 if string invalid
		end
		return total/count
	end


	def process_text(text)
		return text.gsub("?text=","").gsub("%20", " ").gsub(/[!@%&"=?\/.,]/,'')
	end


	def execute(text)
		return get_average_word_length(split_to_words(process_text(text)))
	end

end