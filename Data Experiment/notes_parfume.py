import pandas as pd

# Data as dictionary for each category
data = {
    'Citrus': ["Bergamot", "Lemon", "Orange", "Grapefruit", "Mandarin", "Lime", "Neroli", "Clementine", "Tangerine", "Yuzu", 
               "Pomelo", "Kaffir Lime", "Bitter Orange", "Citron", "Calamondin", "Kumquat", "Blood Orange", "Seville Orange", 
               "Green Mandarin", "Sweet Orange", "Finger Lime", "Rangpur", "Sudachi", "Bergamot Orange", "Meyer Lemon", 
               "Persian Lime", "Key Lime", "Mexican Lime", "Sweet Lemon", "Rough Lemon", "Oroblanco", "Tangor", "Ugli Fruit", 
               "Combava", "Caviar Lime", "Mandarin Petitgrain", "Lemon Verbena", "Lemon Balm", "Lemon Zest", "Lemon Leaf", 
               "Orange Zest", "Orange Leaf", "Grapefruit Zest", "Grapefruit Leaf", "Bergamot Zest", "Bergamot Leaf", "Citrus Peel", 
               "Citrus Blossom", "Kaffir Lime Leaf", "Kumquat Peel"],
    'Flowers': ["Lavender", "Rose", "Jasmine", "Ylang-Ylang", "Iris", "Violet", "Lily of the Valley", "Magnolia", "Peony", 
                "Gardenia", "Honeysuckle", "Tuberose", "Freesia", "Narcissus", "Orchid", "Cherry Blossom", "Camellia", 
                "Daffodil", "Hyacinth", "Lilac", "Orange Blossom", "Osmanthus", "Plumeria", "Poppy", "Carnation", "Sunflower", 
                "Daisy", "Geranium", "Mimosa", "Sweet Pea", "Marigold", "Bluebell", "Anemone", "Hibiscus", "Heliotrope", 
                "Petunia", "Stock", "Viola", "Wisteria", "Primrose", "Lotus", "Morning Glory", "Pansy", "Zinnia", "Snowdrop", 
                "Foxglove", "Alyssum", "Begonia", "Sweet William", "Columbine"],
    'Woods': ["Sandalwood", "Cedarwood", "Patchouli", "Vetiver", "Oakmoss", "Pine", "Guaiac Wood", "Agarwood", "Rosewood", 
              "Ebony", "Mahogany", "Teak", "Birch", "Cypress", "Balsam Fir", "Redwood", "Maple", "Willow", "Moss", "Oud", 
              "Hinoki", "Amberwood", "Frankincense", "Myrtle", "Labdanum", "Cashmere Wood", "Tobacco", "Driftwood", "Juniper", 
              "Cedar", "Palisander Rosewood", "Bamboo", "Silver Fir", "Palo Santo", "Ebony Wood", "Amaris Wood", "Tolu Balsam", 
              "Spruce", "Larch", "Ebony Tree", "Macassar Ebony", "Sipo Mahogany", "African Blackwood", "Bay Laurel", "Hemlock", 
              "Mountain Juniper", "Olibanum", "Tasmanian Oak", "Australian Sandalwood", "Scots Pine"],
    'Fruity': ["Apple", "Peach", "Pear", "Raspberry", "Blackcurrant", "Pineapple", "Mango", "Banana", "Strawberry", "Cherry", 
               "Blueberry", "Melon", "Cranberry", "Passion Fruit", "Kiwi", "Lychee", "Grape", "Pomegranate", "Guava", "Apricot", 
               "Coconut", "Fig", "Plum", "Watermelon", "Nectarine", "Papaya", "Mulberry", "Cassis", "Boysenberry", "Loganberry", 
               "Starfruit", "Tamarind", "Persimmon", "Jujube", "Quince", "Date", "Acai", "Prune", "Rambutan", "Kiwano", "Salak", 
               "Jackfruit", "Mirabelle", "Mangosteen", "Medlar", "Soursop", "Sugar-apple", "Cupuacu", "Durian", "Dragonfruit"],
    'Greens': ["Fig", "Basil", "Thyme", "Green Tea", "Mint", "Cucumber", "Tomato Leaf", "Galbanum", "Clary Sage", "Tarragon", 
               "Grass", "Peppermint", "Spearmint", "Eucalyptus", "Hemp", "Bamboo", "Ivy", "Juniper Leaf", "Laurel Leaf", 
               "Lemongrass", "Pine Needle", "Violet Leaf", "Parsley", "Shiso", "Mate", "Tea Leaf", "Geranium Leaf", "Davana", 
               "Cardamom Leaf", "Blackcurrant Leaf", "Cilantro", "Lovage", "Pine Shoot", "Verbena", "Pepper Leaf", "Celery Leaf", 
               "Dill", "Carrot Leaf", "Tea Tree", "Olive Leaf", "Fennel Leaf", "Clove Leaf", "Costmary", "Ho Leaf", "Lettuce", 
               "Chervil", "Mustard Leaf", "Beet Leaf", "Kale Leaf", "Bay Leaf"],
    'Sweet': ["Vanilla", "Caramel", "Honey", "Cotton Candy", "Maple Syrup", "Marshmallow", "Chocolate", "Praline", "Toffee", 
              "Butterscotch", "Milk", "Sugar", "Hazelnut", "Nougat", "Almond", "Syrup", "Molasses", "Cupcake", "Cake", "Candy", 
              "Cookie", "Jelly Bean", "Licorice", "Cinnamon", "Gingerbread", "Fudge", "Glazed", "Ice Cream", "Meringue", 
              "Macaron", "Pastry", "Pie", "Pudding", "Shortbread", "Snickerdoodle", "S’mores", "Sorbet", "Tart", "Truffle", 
              "Wafer", "Waffle", "White Chocolate", "Yogurt", "Brown Sugar", "Buttermilk", "Churro", "Candy Cane", "Carrot Cake", 
              "Donut", "Éclair"],
    'Aquatic': ["Sea Breeze", "Ocean Water", "Marine Accord", "Salty Air", "Seaweed", "Algae", "Water Lily", "Lotus", "Driftwood", 
                "Coral", "Sea Salt", "Sea Foam", "Kelp", "Marine Salt", "Rainwater", "Wet Stone", "Aquatic Moss", "Sea Spray", 
                "Brine", "Cool Water", "Freshwater", "Marine Air", "Lake Water", "River Water", "Dew", "Water Mint", "Cucumber", 
                "Blue Lagoon", "Pond Water", "Aqua", "Water Accord", "Oceanic", "Seashore", "Wet Sand", "Island Breeze", 
                "Fresh Lagoon", "Bay Water", "Harbour Breeze", "Marine Ozone", "Ice Water", "Arctic Breeze", "Glacier Water", 
                "Deep Sea", "Sea Ice", "Marine Mist", "Cascade Water", "Aqua Marine", "Ocean Mist", "Rainforest Water", "Tidal Wave"]
}

# Convert dictionary to DataFrame and transpose it for better formatting
df = pd.DataFrame.from_dict(data, orient='index').transpose()

# Save DataFrame to CSV file
df.to_csv('parfume_notes.csv', index=False)
