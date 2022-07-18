# app.rb
require 'sinatra'
require 'sinatra/json'
require 'sinatra/cross_origin'

require_relative 'averageWordLength'
include AverageWordLengthMethods

before do
    content_type 'application/json'
end

get '/*' do
	headers 'Access-Control-Allow-Origin' => '*'
	average = execute(request.fullpath)
	if (average == -1)
		json error: true, string: "Error: String invalid or empty", answer: 0
	else
		json error: false, string: "Average word length: " + average.to_s, answer: average
	end
end

# https://www.codewithjason.com/dockerize-sinatra-application/