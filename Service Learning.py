from tkinter import *
import tkinter.font as font


# Making the window widget
root = Tk()
root.geometry("450x450")
root.title("Service Learning")


# Functions
def Submit_form():
    global r
    root.withdraw()
    Screen_1 = Toplevel(root)
    Screen_1.geometry("450x530")
    Screen_1.title("Service Learning")

    p = IntVar()

    # Functions
    def Submit_form_1():
        Screen_1.destroy()
        Screen_2 = Toplevel(root)
        Screen_2.title("Service Learning")

        def Submit_form_2():
            Screen_2.destroy()
            root.deiconify()

        # Heading
        Heading_2 = Label(Screen_2, text="WePlant", padx=40, fg='Green')
        myFont_H_2 = ("Comic Sans MS", 40, "bold")
        Heading_2.grid(row=0, column=1, columnspan=3)
        Heading_2.configure(font=myFont_H_2)

        # Welcome Message
        Level_2 = Label(Screen_2, text="    ")
        Level_2.grid(row=1, column=0)
        message_2 = Label(Screen_2, text="Get to know more about the plants around you")
        myFont_W_2 = ("Arial", 15)
        message_2.grid(row=1, column=1, columnspan=3)
        message_2.configure(font=myFont_W_2)

        # Lists
        Plant_List_Scientific = ["error"]
        Plant_List_Tip = ['error']
        Plant_List_Recognize = ['error']
        if r.get() == 0:
            Plant_List_Scientific = ["Terminalia arjuna", "Saraca asoca ", "Ficus benghalensis", "Murraya koenigii",
                                     "Delonix Regia", "Swietenia mahagoni", "Azadirachta indica ", "Ficus Religiosa "]
            Plant_List_Tip = ["""1.) This is a deciduous tree with conical leaves and bright yellow flowers.
2.) Arjuna tree is generally found around river beds. 
3.) The bark of the tree has Ayurveda properties and has anti-oxidant properties 
4.) It is used to treat heart conditions and for moderating asthma. """,
                              """1.) Ashoka tree is a rain-forest tree and is abundantly found in the central areas
of the Deccan plateau and in parts of the Western Ghats. 
2.) This is famously known for its fragrant flowers, pointed top, and thick foliage
3.) This tree is an evergreen one and is known for its foliage.
4.) Its leaves are dark green in colour and grow in bunches. """,
                              """1.) Banyan tree, originate in India,  is the most familiar shade giving tree in our country. 
2.) It is also considered holy and symbolizes life and fertility 
3.) These Indian trees have the largest canopy coverage in India. 
4.) Not many people know but the banyan tree is also the national tree of India. 
5.) The wood is used in making paper and fastening ropes.""",
                              """1.) Curry tree is a tropical to sub-tropical tree and is native to India and Sri Lanka. 
2.) Its leaves are widely used in south Indian dishes because of their strong aroma. """,
                              """1.) Gulmohar is most famous for its pretty looking flowers. 
2.) This shade giving tree expands and offers a dense canopy. 
3.) The flowers of this tree are large and orange-red in colour. 
4.) It is mostly ornamental and the wood is used for making handles for tools and combs since it is very durable.
5.) It also offers medicinal properties like anti-inflammatory and anti-fungal""",
                              """1.) In India, these trees are mainly found in Thattekkad Wildlife Sanctuary
Kaziranga Wildlife Sanctuary and Corbett National Park. 
2.) The bark of this tree is typically used for making musical instruments and furniture.
3.) It provides shade and shelter to many animals and also purifies air at a rapid rate""",
                              """1.) Most popular and one of the best trees to plant near house in India.
2.) It is grown in both tropical and sub-tropical regions. 
3.) Neem has many medicinal values and healing properties
4.) It is used to control pests in farming. 
5.) Neem is a major ingredient in soaps and shampoos and is healthy for our skin.""",
                              """1.) This is one of those rare trees of India that release oxygen both in the day and the night. 
2.) This is an evergreen tree and is also worshipped in many parts of the country.
3.) The leaves of the tree are used to deal with asthma, stomach pain, and heart issues.
4.) Eating ripe fruits of the tree is helpful in improving a poor appetite. """]
            Plant_List_Recognize = ["1.) The woody fruit has five wings and is possibly the most unique looking fruit",
                                    """1.) Its leaves grow in dense clusters and are pointed from the top.
2.) The flowers grow in heavy bunches as well.
3.) They are bright yellow and orange in color.""",
                                    """1.) It has a large canopy and aerial prop roots.
2.) If you pluck a leaf, a white sticky liquid is visible. """,
                                    """1.) It is a small tree growing up to 6 metres. 
2.) Its leaves are pinnate and have 11-21 leaflets. 
3.) The plant produces small white flowers that self pollinate and produce small black berries. """,
                                    """1.) Its leaves are doubly pinnate. 
2.) Each leaf is approximately 40 cm long and has 20-40 pairs of primary leaflets.
3.) They are feathery in appearance and bright, light green in colour.""",
                                    """1.) The tree is generally 30-40 feet in height. 
2.) Its fruit resembles a large greenish capsule and its wood is red brown in colour. """,
                                    """1.) It has a strong smell and its flowers are pale white in colour. 
2.) Its leaves grow in pairs along a long common stem.""",
                                    "1.) The leaves of this tree are heart-shaped with an extended drip tip."]
        elif r.get() == 1:
            Plant_List_Scientific = ["Bougainvillea", "Dahlia", "Aerides", "Hibiscus rosa-sinensis", "Jasminum",
                                     "Nelumbo nucifera", "Tagetes", "Viola tricolor var"]
            Plant_List_Tip = ["""1.) Commonly found surrounding the front doors
2.) These flowers are known as the paper-flowers in Bengali as the texture of these flowers is similar to paper. 
3.) They grow all the year around and appear to be similar to bushes.""",
                              """1.) A beautiful addition to one’s garden. Dahlias are gorgeous and elegant. 
2.) They’re also known to be great summer flowers in India. 
3.) There are often flower competitions where this flower is showcased.""",
                              """1.) Another exotic flower that’s available in India.
2.) They’re also known as Cat’s-tail Orchids.
3.) Fragrant and colorful, they make for great house-plants and garden flowers.""",
                              """1.) Another flower that is widely used for worshipping is Hibiscus. 
2.) It is known to be the flower of Goddess Kali and is an essential item to be used to adorn her idol. 
3.) Their bright red color is empowering on the goddess. 
4.) This flower is commonly found in various regions within India and they grow all the year around.""",
                              """1.) This flower is known for its unique sweet smell. 
2.) Widely used in cosmetic products and even in Ayurveda, the smell of jasmine is calming and soothing. 
3.) They are also widely used in weddings and social events. 
4.) They bloom from spring to fall with a resting period in October.""",
                              """1.) A common water plant known as Lotus or Water-lily. 
2.) This flower is also associated with the Indian God Brahma who is often seen placed on this flower. 
3.) They begin to grow in early April. In late June and mid-August, they reach full bloom.""",
                              """1.) Widely used for worshipping purpose, Marigold is ancient in Indian history, it’s also used in Hindu weddings. 
2.) Their bright yellow color has a very cheerful vibe to them. 
3.) These flowers can withstand the Indian heat; perfect for summer & autumn gardening.""",
                              """1.) It is available throughout the year in India but usually planted in winter or fall. 
2.) They are colorful and vibrant, a great addition to one’s garden. 
3.) They are also known to be the valley flowers."""]
            Plant_List_Recognize = ["""1.) Bougainvilleas have very distinctive blooms that come in hot pink, salmon, purple or yellow. 
2.) What appear to be flowers are actually papery, leaf-like bracts.
3.) Bougainvilleas have long, elliptical leaves and 1- to 2-inch thorns.""",
                                    """1.) Dahlias spread their showy florets.
2.) Hot colors like pinks, reds, yellows, and even purples in blooms the size up to a dinner plate. 
3.) Characterized by a single flower-headed stem that is also leafy""",
                                    """1.) Fox Brush Orchid is a dwarf orchid species with crystalline pink, spotted magenta, fragrant flowers to 2cm. 
2.) The spikes are arching to pendulous, to about 25cm long with many flowers""",
                                    """1.) They are ovate with finely serrated margins. 
2.) The solitary flowers come in many colors. 
3.) They have five petals, a bell shaped calyx, and a long, conspicuous column of stamens.""",
                                    """1.) They can be summer or winter flowering, with flowers that are white, yellow and occasionally red and pink. 
2.) All jasmines have small star-shaped flowers with a sweet and distinctive fragrance.""",
                                    """1.) The aquatic sacred lotus plant is grown worldwide for its 8-inch-wide showy flowers.
2.) It's roundish and upward-cupped waxy green leaves that can reach 2 feet across.""",
                                    """"1.) Flowers may have only five petals surrounding a yellow-orange center or a cluster 
of petals that looks like a pompom.
2.) Marigold leaves are dark green and deeply divided, giving them a ferny appearance.""",
                                    """1.) Pansy flowers are single with five petals that are rounded in shape. 
2.) Pansy flowers have one of three basic color patterns."""]
        elif r.get() == 2:
            Plant_List_Scientific = ["Aloe vera", 'Bacopa monieri', "Coriandrum sativum", "Foeniculum vulgare",
                                     "Trigonella foenum-graecum", "Zingiber officinale", "Mentha", "Ocimum tenuiflorum"]
            Plant_List_Tip = ["""1.) In Ayurveda, aloe vera is known as the 'King of medicinal plants.' 
2.) It holds water in its fleshy leaves which is why it can sustain in extremely dry conditions as well. 
3.) It surely can treat a wide variety of health problems.""",
                              """1.) It is a staple herb in Ayurvedic medicine.
2.) It has strong anti-inflammatory properties that are as effective as common NSAIDs""",
                              """1.) Coriander or dhania is an important ingredient of an Indian kitchen. 
2.) Its leaves, seeds and powder of the seeds, everything is beneficial for your health. """,
                              """1.) Fennel or saunf is a flavorful and aromatic plant which is useful for a wide variety of health problems. 
2.) In India, people are accustomed to chewing fennel seeds after every meal.""",
                              """1.) Methi or fenugreek is a wonder amongst other medicinal plants, and all because of its properties. 
2.) It is an evergreen plant and both the leaves and the seeds are useful.""",
                              """1.) It is the root solution for a wide variety of health problems. 
2.) It is an important ingredient of Indian food due to its distinct flavor, and of course, its benefits for your overall health""",
                              """1.) This freshly fragrant medicinal plant serves a wide variety of purposes. 
2.) This plant requires a lot of water to grow. """,
                              """1.) Tulsi is the Queen of medicinal plants. 
2.) This plant holds immense significance in the Hindu religion. 
3.) The strong aroma of Tulsi is good enough to keep bacterial growth at bay. """]
            Plant_List_Recognize = ["""1.) Constipation
2.) Poor body immunity""",
                                    """1.) Improvements in learning rates, attention and memory
2.) Improving body’s ability to deal with stress and anxiety.""",
                                    """1.) It is rich in antioxidants
2.) Cures urine retention
3.) Treats acne """,
                                    """1.) Treats cough
2.) Controls cholesterol
3.) Cure acidity """,
                                    """1.) Controls cholesterol levels
2.) Purifies blood
3.) Beneficial for joint pains and diabetes """,
                                    """1.) Treats indigestion
2.) Controls blood pressure
3.) Treats cold, cough, flu and asthma """,
                                    """1.) Keeps the digestive system running
2.) Boosts immunity
3.) Benefits respiratory health """,
                                    """1.) Treats cough
2.) Anti-cancer """]

        # Info Frame
        frame_2 = LabelFrame(Screen_2, padx=10, pady=10)
        frame_2.grid(row=2, column=1, columnspan=3, padx=10, pady=10)

        # Info

        Scientific = Label(frame_2, text=f"Scientific Name - {Plant_List_Scientific[p.get()]}", anchor='w')
        Scientific.grid(row=0, column=0)
        Tip = Label(frame_2, text=f"""Information:
{Plant_List_Tip[p.get()]}""", anchor='w')
        Tip.grid(row=1, column=0)
        if r.get() == 0 or r.get() == 1:
            Recognize = Label(frame_2, text=f"""How to recognize it:
{Plant_List_Recognize[p.get()]}""", anchor='w')
            Recognize.grid(row=2, column=0)
        elif r.get() == 2:
            Recognize_1 = Label(frame_2, text=f"""Benefits:
{Plant_List_Recognize[p.get()]}""", anchor='w')
            Recognize_1.grid(row=2, column=0)

        # Submit
        myFont1 = font.Font(size=10)
        Submit_2 = Button(Screen_2, text="Back", command=Submit_form_2, padx=10, font=myFont1)
        Submit_2.grid(row=4, column=1, padx=10, pady=3, columnspan=3)

        # Exit
        Exit_2 = Button(Screen_2, text='Exit', command=root.destroy, padx=10)
        Exit_2.grid(row=3, column=1, pady=3, columnspan=3)

    # Heading
    Heading_1 = Label(Screen_1, text="WePlant", padx=40, fg='Green')
    myFont_H_1 = ("Comic Sans MS", 40, "bold")
    Heading_1.grid(row=0, column=0, columnspan=3)
    Heading_1.configure(font=myFont_H_1)

    # Welcome Message
    Level_1 = Label(Screen_1, text="    ")
    Level_1.grid(row=1, column=0)
    message_1 = Label(Screen_1, text="Get to know more about the plants around you")
    myFont_W_1 = ("Arial", 15)
    message_1.grid(row=1, column=1)
    message_1.configure(font=myFont_W_1)

    # List of Plants
    Plant_List = ["error"]
    if r.get() == 0:
        Plant_List = ["Arjuna tree", "Ashoka Tree", "Banyan tree", "Curry tree", "Gulmohar tree", "Indian Mahogany",
                      "Neem", "Peepal tree"]
    elif r.get() == 1:
        Plant_List = ["Bougainvillea", "Dahlia", "Fox Brush Orchid", "Hibiscus", "Jasmine", "Lotus", "Marigold",
                      "Pansy"]
    elif r.get() == 2:
        Plant_List = ["Aloe vera", 'Brahmi', "Coriander", "Fennel", "Fenugreek", "Ginger", "Mint", "Tulsi"]

    # Frame for input
    frame_1 = LabelFrame(Screen_1, padx=10, pady=10)
    frame_1.grid(row=3, column=1, columnspan=3, padx=10, pady=10)

    # Input
    myFont_2 = font.Font(size=12)
    Radiobutton(frame_1, text=Plant_List[0], variable=p, value=0, padx=8, pady=2, font=myFont_2).grid(row=0, column=0)
    Radiobutton(frame_1, text=Plant_List[1], variable=p, value=1, padx=8, pady=2, font=myFont_2).grid(row=1, column=0)
    Radiobutton(frame_1, text=Plant_List[2], variable=p, value=2, padx=8, pady=2, font=myFont_2).grid(row=2, column=0)
    Radiobutton(frame_1, text=Plant_List[3], variable=p, value=3, padx=8, pady=2, font=myFont_2).grid(row=3, column=0)
    Radiobutton(frame_1, text=Plant_List[4], variable=p, value=4, padx=8, pady=2, font=myFont_2).grid(row=4, column=0)
    Radiobutton(frame_1, text=Plant_List[5], variable=p, value=5, padx=8, pady=2, font=myFont_2).grid(row=5, column=0)
    Radiobutton(frame_1, text=Plant_List[6], variable=p, value=6, padx=8, pady=2, font=myFont_2).grid(row=6, column=0)
    Radiobutton(frame_1, text=Plant_List[7], variable=p, value=7, padx=8, pady=2, font=myFont_2).grid(row=7, column=0)

    # Submit
    myFont_3 = font.Font(size=15)
    Submit_3 = Button(Screen_1, text="Let's Proceed", command=Submit_form_1, padx=10, font=myFont_3, fg="Green")
    Submit_3.grid(row=4, column=1, padx=10, pady=7)

    # Exit
    Exit_1 = Button(Screen_1, text='Exit', command=root.destroy, padx=10)
    Exit_1.grid(row=5, column=1, pady=5)


# Variables
r = IntVar()

# Heading
Heading = Label(root, text="WePlant", padx=40, fg='Green')
myFont_H = ("Comic Sans MS", 40, "bold")
Heading.grid(row=0, column=0, columnspan=3)
Heading.configure(font=myFont_H)

# Welcome Message
Level = Label(root, text="    ")
Level.grid(row=1, column=0)
message = Label(root, text="Get to know more about the plants around you")
myFont_W = ("Arial", 15)
message.grid(row=1, column=1)
message.configure(font=myFont_W)

# Frame for input
frame = LabelFrame(root, padx=10, pady=10)
frame.grid(row=3, column=1, columnspan=3, padx=10, pady=10)

# Input
myFont_1 = font.Font(size=12)
Radiobutton(frame, text='Trees in India', variable=r, value=0, padx=8, pady=5, font=myFont_1).grid(row=0, column=0)
Radiobutton(frame, text='Flowers in India', variable=r, value=1, padx=8, pady=5, font=myFont_1).grid(row=1, column=0)
Radiobutton(frame, text='Medicinal herbs in India', variable=r, value=2, padx=8, pady=5, font=myFont_1).grid(row=2,
                                                                                                             column=0)

# Submit
myFont = font.Font(size=15)
Submit = Button(root, text="Let's Proceed", command=Submit_form, padx=10, font=myFont, fg="Green")
Submit.grid(row=4, column=1, padx=10, pady=10)

# Exit
Exit = Button(root, text='Exit', command=root.destroy, padx=10)
Exit.grid(row=5, column=1, pady=5)

# Quote
Quote = """Never say there is nothing beautiful in the world anymore.
There is always something to make you wonder
in the shape of a tree, the trembling of a leaf."""

Level_Q_1 = Label(root, text='')
Level_Q_1.grid(row=6, column=1)

myFont_Quote = font.Font(size=12)
Quote_Label = Label(root, text=Quote, fg="Grey", font=myFont_Quote)
Quote_Label.grid(row=7, column=1, columnspan=3)
# Creating the main loop
root.mainloop()
