require_relative 'app.rb'

require 'test/unit'
require 'rack/test'
require 'json'

ENV['ENV_ENV'] = 'test'

class ServerTest < Test::Unit::TestCase
  include Rack::Test::Methods
  
  def app
    Sinatra::Application
  end
  
  def test_it_gets_correct_response
    get '/hello'
    assert last_response.ok?
    resp = JSON.parse(last_response.body)
    assert 5 == resp["answer"]
    assert false == resp["error"]
    assert "Average word length: 5" == resp["string"]
  end
end

# http://sinatrarb.com/testing.html
# https://ruby-doc.org/stdlib-2.6.3/libdoc/json/rdoc/JSON.html