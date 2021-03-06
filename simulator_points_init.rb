points = []
# 4 strings of 30 each
# 2 strings of 240 each (output split in 2 for this)
x = 0.0
y = 0.0
z = 2.0
r = 2.0
spacing = 10.0 / 210.0
spacing_2 = z / 30.0

(0..3).each do |i|
  (0..29).each do |j|
    radius = r - (j * spacing_2)
    points << [radius * Math.cos((i * Math::PI) / 3.0 ), radius * Math.sin((i * Math::PI) / 3.0), j * spacing_2]
  end
  (30..63).each do |j|
    points << [0, 0, 0]
  end
end

(0..29).each do |j|
  radius = r - (j * spacing_2)
  points << [radius * Math.cos((4 * Math::PI) / 3.0 ), radius * Math.sin((4 * Math::PI) / 3.0), j * spacing_2]
end

(0..209).each do |i|
  points << [x, y, i * spacing + z]
end

(0..15).each do |i|
  points << [0, 0, 0]
end


puts "["
points[0...-1].each do |point|
  puts "  {\"point\": [#{point[0]}, #{point[1]}, #{point[2]}]},"
end

last = points.last
puts "  {\"point\": [#{last[0]}, #{last[1]}, #{last[2]}]}"

puts "]"
