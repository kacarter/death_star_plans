points = []
# 6 strings of 30 each
# 1 string of 210 each
x = 0.0
y = 0.0
z = 2.0
r = 2.0
spacing = 14.0 / 210.0
spacing_2 = z / 30.0

(0..5).each do |i|
  (0..29).each do |j|
    radius = r - (j * spacing_2)
    points << [radius * Math.cos((i * Math::PI) / 3.0 ), radius * Math.sin((i * Math::PI) / 3.0), j * spacing_2]
  end
end

(0..209).each do |i|
  points << [x, y, i * spacing + z]
end


puts "["
points[0...-1].each do |point|
  puts "  {\"point\": [#{point[0]}, #{point[1]}, #{point[2]}]},"
end

last = points.last
puts "  {\"point\": [#{last[0]}, #{last[1]}, #{last[2]}]}"

puts "]"
