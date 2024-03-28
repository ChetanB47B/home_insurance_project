QUESTION = {"Exterior": """
        You are a property inspector please analyse image and below are the questions and each questions has there multiple choice answer,
        please give me answer in json format keep question as a key and answer is value 
        
        for example answer {"Q1 - Excessive garbage on premises":here is your answer, "Q2 - Are trees overhanging the roof, IVY or BUSH growing into house?" : here is your answer ....... }


        Q1 - Excessive garbage on premises
        Options - Yes, No
        
        Q2 - Are trees overhanging the roof, IVY or BUSH growing into house?
        Options - Yes, No
        
        Q3 - Self - latching gate or frnce present and operable
        Options - Yes, No
        
        Q4 - Any sidewalks very uneven         
        Options - Yes, No
        
        Q5 - New Home Under Construction
        Options - Yes, No
        
        Q6 -  Construction type
        Options -  Asbestos/Stucco, Frame, Fire Resistive, Log, Masonry, Masonry Veneer
        
        Q7 - Number of Stories        
        Options - 1 Story, 1 1/2 Stories (Attic), 2 Stories, 21/2 Stories (Attic), 3 Stories, 31/2 Stories (Attic), 4 Stories, Bi-Level (Raised Ranch), Split Level
        
        Q8 - Roof shape
        Options - Complex/Custom,Flat,Gable ,Gambrel,Mansard ,Total Hip ,Unable to Determine
        
        Q9 - Flat roof exhibiting tears, blisters, patches, ponding, or deterioration
        Options - No,Major ,Minor
        
        Q10 - Number of roof layers (Assess from side of roof when possible)
        Options - 1,2,3 or more
        
        Q11 - Any attached garages         
        Options - Yes, No, None, 1.5 Car (396 SF), 1 Car (280 SF), 2 Car (576 SF), 25 Car (672 SF), 3 Car (780 SF), 3.5 Car (884 SF), 4 Car (1040 SF), 4.5 Car (1144 SF), 5 Car (1248 SF), 5.5 Car (1404 SF), 6 Car (1512 SF), 6.5 Car (1674 SF), 7 Car (1782 SF), 7.5 Car (1890 SF), 8 Car (1998 SF), 8.5 Car (2160 SF)                                                                                                                                                 
        
        Q12 - Roof Cover        
        Options - Built-up Hot Mopped w/Gravel, Built-up Hot Mopped w/o Gravel, Composition 3 Tab , Composition Architectural Shingle, Composition Impact Resistive Shingle, Composition Roll Roofing, Composition over Wood Shingle or Shake, Discontinued/Obsolete Roofing Material (i.e. Asbestos, T-Lock, etc.), Membrane-EPDM or PVC,Metal - Copper Shingle, Metal - Corrugated Galvanized, Metal-Painted Rib, Metal - Standing Seam, Metal - Standing Seam Copper, Metal - Tile/Shake, Slate,Sprayed Polyurethane Foam(SPF), Synthetic Composite Roofing, Tile - Cement Fiber, Tile - Clay, Tile - Concrete, Tile - Glazed, Wood Shingles or Shakes, Wood Shingles or Shakes Deco Pattern
        
        Q13 - Is there any Junked cars present outside
        Options - Yes, No
        
        Q14 - Are there any appliances on the exterior of house (I.E. range, refrigerator, oven, etc.)
        Options - Yes, No
        
        Q15 - Is there any excessive garbage on house premises
        Options - Yes, No
        
        Q16 - Is there any other debris present outside the house
        Options -  Yes, No
        
        Q17 - Is there any Commercial farm equipment and/or large farm buildings and silos present
        Options - Yes, No
        
        Q18 - Is there a swimming pool
        Options - yes, No
        
        Q19 - If swimming Pool is there what's the type ?
        Options - Above Ground, In Ground, Unable to Determine
        
        Q20 -If swimming Pool is there what's the condition?
        Options - Good, Poor, Unable to Determine
        
        Q21 - If swimming Pool is there Pool fenced
        Options - Yes, No, Unable to Determine
        
        Q22 - Is there a trampoline
        Options - Yes, No
        
        Q23 - If trampoline is there what's the condition?
        Options - yes, No, Unable to Determine
        
        Q24 - Is there a skateboard ramp
        Options - yes, No
        
        Q25 - Is there is a skateboard ramp what's the condition?
        Options - yes, No, Unable to Determine
        
        Q26 - Is there a zipline?
        Options - yes, No, Unable to Determine
        
        Q27 - If zipline is there what's the condition of zipline?
        Options - Good, Poor, Unable to Determine
        """,

        "Chimney": """
            You are a property inspector please analyse image and below are the questions and each questions has there multiple choice answer,
            please give me answer in json format keep question as a key and answer is value 
            
            For example answer {"Q1 - Is there a masonry chimney":here is your answer, "Q2 - Does chimney have missing, damaged, or deteriorating flashing" : here is your answer ....... }

           Q1 - Is there a masonry chimney
           Options - Yes, No
        
           Q2 - Does chimney have missing, damaged, or deteriorating flashing
           Options - Yes, No
        
           Q3 - Is chimney structurally unsound, have a deteriorating cap, or crumbling bricks?
           Options - Yes, No
        
           Q4 - Is chimney leaning or pulling away from house
           Options - Yes, No
        """,

    "Roof": """
            You are a property inspector please analyse image and below are the questions and each questions has there multiple choice answer,
            please give me answer in json format keep question as a key and answer is value 
            
            For example answer {"Q1 - What's the roof shape":here is your answer, "Q2 - Were you unable to determine the roof covering type (I.E. You cant see the roof due to snow, roof height, etc.)" : here is your answer ....... }

            Q1 - What's the roof shape
            Options - Flat, Gable, Gambrel, Mansard, Total Hip, Unable to Determine	
             
            Q2 - Were you unable to determine the roof covering type (I.E. You cant see the roof due to snow, roof height, etc.)
            Options - Yes, No, Partial
             
            Q3 - Percentage of roof unable to determine Roof Cover type
            Options - Please review manually for suggestions as I'm not sure
             
            Q4 - Number of roof layers (Assess from side of roof when possible)
            Options - Please review manually for suggestions as I'm not sure
             
            Q5 - Is there any Shingles curling and/or splitting?
            Options - No, Major, Minor, NA
             
            Q6 - Any Impact marks on shingles? 
            Options - No, Major, Minor, NA
             
            Q7 - Any Missing shingles?
            Options - No, Major, Minor, NA
             
            Q8 - Is there Uneven roof surface?
            Options - No, Major, Minor, NA
             
            Q9 - Flat roof exhibiting tears, blisters, patches, ponding, or deterioration
            Options - No, Major, Minor, NA
             
            Q10 - Algae, moss, mildew, fungus/mold or other growths on any type of roof
            Options - No, Major, Minor, NA
        """,

    "Animal present": """
        You are a property inspector please analyse image and below are the questions and each questions has there multiple choice answer,
        please give me answer in json format keep question as a key and answer is value 
            
        For example answer {"Q1 - Any dogs on premises":here is your answer, "Q2 - Horses Present" : here is your answer ....... }

        Q1 - Any dogs on premises
        Options - Yes, No
        
        Q2 -Is there any horses Present?
        Options - Yes, No
        
        Q3 - How many horses on site?
        Options - Can't be answered 
        
        Q4 - Is there any cattle present?
        Options - Yes, No
        
        Q5 - How many cattle on site?
        Options - Can't be answered 
        
        Q6 - Is there any other animals capable of causing injury or damaging property?
        Options - Yes, No
        

    
    """,
    "Foundation": """
        You are a property inspector please analyse image and below are the questions and each questions has there multiple choice answer,
        please give me answer in json format keep question as a key and answer is value 
            
        For example answer {"Q1 - Were you unable to determine the foundation type (i.e., Your view of the foundation is fully blocked by ivy, snow, etc.)":here is your answer, "Q2 - Horses Present" : here is your answer ....... }
    
        Q1 - Were you unable to determine the foundation type (i.e., Your view of the foundation is fully blocked by ivy, snow, etc.)
        Options - Yes,No
        
        Q2 - What is the foundation type?
        Options - Basement,Crawlspace,Concrete Slab,Elevated Post/Pier and Beam(Stilts),Stilts with Sweep Away Walls,Shallow Basement,Pier and Grade Beam,Deep Pilings
        
        Q3 - What is the foundation shape?
        Options - 4-5 Corners Square/Rectangle,6-7 Corners - L Shape,8-10 Corners - T,U ,Z Shape,11-12 Corners-H or Custom Shape,13+ Corners - Irregular/Complex
        
        Q4 - Is Foundation needs repair?
        Options - Yes,No
       
        Q5 - Is there any large foundation cracks?
        Options - Yes,No
        
        Q6 - Is foundation leaning?
        Options - Yes,No
        
        Q7 - Is there evidence of settling?
        Options - No,Yes - Major Settling,Yes - Minor Settling
    """,

    "Porches" : """
        You are a property inspector please analyse image and below are the questions and each questions has there multiple choice answer,
        please give me answer in json format keep question as a key and answer is value 
            
        For example answer {"Q1 - Do porches or decks need repair?" : here is your answer, "Q2 - Are there any porches or decks missing a rail where needed (3 ft. fall hazard)" : here is your answer ....... }
    
        Q1 - Do porches or decks need repair?
        Options - Yes,No
        
        Q2 - Are there any porches or decks missing a rail where needed (3 ft. fall hazard)
        Options - Yes,No
        
        Q3 - Are porches or decks pulling away from the house
        Options - Yes,No
        
        Q4 - Are porches or decks missing boards
        Options - Yes,No
    
        Q6 - Are handrails/steps missing, deteriorated, or have damaged components (Note: Handrails are required if there are 4 or more risers)
        Options - Yes,No
        
        Q7 - Are handrails/steps pulling away from the house
        Options - Yes,No
        
        Q8 - Any broken/boarded glass
        Options - Yes,No
    """
}




undetermined = ["Property Slope (ONLY select Moderate or Steep if the slope is INTENSE-remember a black diamond ski slope is 40%)",
                "Patch type",
                "Describe damage to metal roof",
                "Any attached garages -- it can be anwered  only yes or no",
                "Describe any other animals capable of causing injury or damaging property",
                "Describe other debris",
                "Property for sale",
                "Explain evidence of business",
                "Rental property",
                "Number of family units",
                "Percentage of the Property that is 1 Story",
                "Percentage of the Property that is crawlspace",
                "Percentage of the Property that is Siding Vinyl",
                "Percentage of the Property that is Brick Veneer",
                "Percent of roof cover that is Composition Architectural Shingle",
                "Do you have comments to add?",
                "Comments",
                "Were you able to complete this survey?",
                "Do porches or decks have inadequate support",
                "Fireplace insert, wood stove, pellet stove, wood-fired furnace, or other wood/solid-fuel burning appliance present"
                ]


LEFTOVER_QUESTIONS = {"Others ": """
                                Q1 - Is the construction complex, oddball, or atypical (non-conventional)?
                                Options - Yes,No
                                
                                Q2 - Are major renovations currently in progress?
                                Options - Yes,No
                                
                                Q3 - Is residence vacant (only select Yes if house is empty or condemned by city)
                                Options - Yes,No
                                
                                Q4 - If over 1 story or occupied basement, are there a minimum of 2 forms of egress from each floor or basement
                                Options - Yes,No
                                
                                Q5 - Were you unable to determine the number of stories (I.E. You cannot see the house)
                                Options - Yes,No
                                
                                Q6 - Were you unable to determine the exterior wall finish (LE. The finish is blocked and not able to be viewed due to ivy, snow, etc.)
                                Options - Yes,No
                                
                                Q7 -  What is the exterior wall finish of the house?
                                Options - Siding - Alum. or Metal, Siding - Vinyl, Siding - Vinyl Shingles, Siding - Hardboard/Masonite, Siding - Plywood (Vertical Groove), Siding Board and Batten, Siding - Cedar (Clapboard), Siding - Cedar (Tongue and Groove), Siding - Redwood (Clapboard), Siding - Redwood (Tongue and Groove), Siding - Pine (Clapboard), Siding - Pine (Tongue and Groove), Siding - Cement Fiber (Clapboard), Cement Fiber (Shingle), Wood Shingle/Shake, Wood Shingle/Shake (Scalloped), Cypress-Reclaimed, Siding - Log, Solid Log - Small (6"-8"), Solid Log - Medium (9-12"), Solid Log - Large (13" or more), Stucco - Synthetic (EFIS), Stucco - Traditional Hardcoat, Brick Veneer, Brick Veneer - Custom, Brick - Solid, Brick - Solid - Custom, Solid Stone, Stone Veneer (Natural), Stone Veneer (Manufactured), Cut Limestone Veneer, Concrete Block - Decorative, Metal - Copper Shingle, Metal - Painted Ribber, Metal - Corrugated Galvanized, None - Included In Ext. Wall Construction,
                                
                                Q9 - Is exterior wall finish damaged
                                Options - Yes,No
                                
                                Q10 - Is exterior wall finish missing
                                Options - Yes,No
                                
                                Q11 - Is exterior wall finish deteriorated
                                Options - Yes,No
                                
                                Q12 - Is there a lack of ventilation?
                                Options: No, Major, Minor, NA
                                
                                Q13 - Is there Granule loss?
                                Options: No, Major, Minor, NA
                                
                                Q14 - Has roof been patched or repaired	
                                Options: No, Major, Minor, NA
                                
                                Q15 - Is there any damage to metal roof?
                                Options: No, Major, Minor, NA
                                
                                Q16 - Are gutters deteriorated, damaged, or missing components
                                Options - Yes,No
                                
                                Q17 - Do downspouts direct water away from the foundation
                                Options - Yes,No
                                
                                Q18 - Are gutters and downspouts clogged
                                Options - Yes,No
                                
                                Q19 - Are soffits/fascia/eaves missing
                                Options - Yes,No
                                
                                Q20 - Are soffits/fascia/eaves deteriorated and or damaged (does not include cosmetic damage like peeling paint)
                                Options - Yes,No
                                
                                Q21 - Are there any attached garages?
                                Options - Yes, No, None, 1.5 Car (396 SF), 1 Car (280 SF), 2 Car (576 SF), 2.5 Car (672 SF), 3 Car (780 SF), 3.5 Car (884 SF), 4 Car (1040 SF), 4.5 Car (1144 SF), 5 Car (1248 SF), 5.5 Car (1404 SF), 6 Car (1512 SF), 6.5 Car (1674 SF), 7 Car (1782 SF), 7.5 Car (1890 SF), 8 Car (1998 SF), 8.5 Car (2160 SF)
                                
                                Q22 - Do sidewalks/walkways need repair
                                Options - Yes,No
                                
                                Q23 - Any sidewalks broken/crumbling
                                Options - Yes,No
                                
                                Q24 - What is the overall condition of detached structures?
                                Options - In need of repair, OK, NA
                                
                                Q25 - Is there playground equipment
                                Options - Yes, No, Unable to Determine
                                
                                Q26 - What is the condition of the playground equipment?
                                Options -  Good, Poor
                                
                                Q27 - Is there overgrown/unkempt brush?
                                Options - Yes,No
                                
                                Q28 - Is the retaining wall in disrepair?
                                Options - Yes,No
                                
                                Q29 - Are there metal security bars on windows with no quick release?
                                Options - Yes,No
                                
                                Q30 - Did you knock or ring doorbell?
                                Options - Yes,No
                                
                                Q31 - Is it a mobile home?
                                Options - Yes,No
                                
                                Q32 - Is there evidence of business on the premises?
                                Options - Yes,No
                                
                                """

}