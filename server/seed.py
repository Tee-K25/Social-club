from faker import Faker
from models import User, Event, Following, Review, Attended ,db
from random import randint
from app import app
from datetime import datetime
fake = Faker()

events = [
    {
        "title": "Gastronomy Gala 2024: A Feast for the Senses",
        "description": "Indulge in an unparalleled culinary journey at Gastronomy Gala 2024, where flavors come alive, and creativity knows no bounds. This extravagant event is a celebration of gastronomic excellence, curated to enchant all your senses. Immerse yourself in a world of exquisite dishes crafted by master chefs, each bite telling a story of innovation and tradition. The culinary demonstrations will offer an insider's glimpse into the artistry behind creating culinary masterpieces. Connect with top chefs, food enthusiasts, and connoisseurs in an atmosphere of elegance and discovery. Gastronomy Gala 2024 is not just a feast for the palate; it's an immersive experience that will leave an indelible mark on your appreciation for fine dining.",
        "date": datetime.strptime(fake.date(), '%Y-%m-%d').date(),
        "time": datetime.strptime(fake.time(), '%H:%M:%S').time(),
        "location": "London",
        "user_id": randint(1, 10),
        "image": "https://images.unsplash.com/photo-1536392706976-e486e2ba97af?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    },
    {
        "title": "AutoFest 2024: Rev Up Your Passion for Cars",
        "description": "Rev up your engines and experience the epitome of automotive excellence at AutoFest 2024. This spectacular event transcends traditional car showcases, offering a journey through the evolution of automotive innovation. From classic beauties to the latest cutting-edge models, AutoFest 2024 is a car lover's paradise. Engage with interactive displays that highlight the intricate details and groundbreaking technology behind each vehicle. Expert talks from industry leaders will provide insights into the future of the automotive world. Whether you're a seasoned car enthusiast or a curious onlooker, AutoFest 2024 promises an immersive experience that will ignite your passion for all things automotive.",
        "date": datetime.strptime(fake.date(), '%Y-%m-%d').date(),
        "time": datetime.strptime(fake.time(), '%H:%M:%S').time(),
        "location": "Monaco",
        "user_id": randint(1, 10),
        "image": "https://images.unsplash.com/photo-1691945901349-5713cc82ffaa?q=80&w=1469&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    },
    {
        "title": "SportsFusion Expo: Where Passion Meets Play",
        "description": "Prepare for an adrenaline-pumping experience at SportsFusion Expo, where passion and play converge in an electrifying atmosphere. This expo is a celebration of the diverse world of sports, bringing together enthusiasts and professionals alike. Immerse yourself in interactive games that let you test your skills and discover new sports. Expert panels featuring renowned athletes will offer unique insights into the intersection of passion and competition. SportsFusion Expo is not just an event; it's a dynamic fusion of excitement, camaraderie, and the joy of play across various sports.",
        "date": datetime.strptime(fake.date(), '%Y-%m-%d').date(),
        "time": datetime.strptime(fake.time(), '%H:%M:%S').time(),
        "location": "Istanbul",
        "user_id": randint(1, 10),
        "image": "https://images.unsplash.com/photo-1667063540150-ff4865d1ad76?q=80&w=1374&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    },
    {
        "title": "Epicurean Elegance Soirée: A Night of Culinary Excellence",
        "description": "Step into an enchanting world of culinary refinement at the Epicurean Elegance Soirée. This exceptional evening is a symphony of flavors and elegance, curated to delight the most discerning palates. Indulge in a gastronomic journey featuring gourmet delights paired with meticulously selected wines. The soirée provides a rare opportunity to connect with culinary connoisseurs, chefs, and fellow enthusiasts in an atmosphere of sophistication. Every dish is a masterpiece, and every sip is an invitation to savor the essence of culinary excellence. The Epicurean Elegance Soirée promises an unforgettable night of indulgence and refined taste.",
        "date": datetime.strptime(fake.date(), '%Y-%m-%d').date(),
        "time": datetime.strptime(fake.time(), '%H:%M:%S').time(),
        "location": "Paris",
        "user_id": randint(1, 10),
        "image": "https://images.unsplash.com/photo-1695606452818-e70080df9e4e?q=80&w=1374&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    },
    {
        "title": "MotorXpo: Unveiling the Pinnacle of Automotive Innovation",
        "description": "Embark on a journey through the evolution of automotive excellence at MotorXpo. This remarkable expo goes beyond the surface, offering an in-depth exploration of the pinnacle of automotive innovation. From sleek designs to groundbreaking technology, each exhibit showcases the future of transportation. Engage with interactive displays that allow you to experience the intricacies of cutting-edge vehicles. Expert talks from industry insiders will shed light on the driving force behind these innovations. MotorXpo is not just an expo; it's a celebration of the passion and ingenuity that drive the automotive world forward.",
        "date": datetime.strptime(fake.date(), '%Y-%m-%d').date(),
        "time": datetime.strptime(fake.time(), '%H:%M:%S').time(),
        "location": "Ontario",
        "user_id": randint(1, 10),
        "image": "https://images.unsplash.com/photo-1695159860063-f4fbc4dd1444?q=80&w=1374&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    },
    {
        "title": "Athlete's Ascent Summit: Scaling New Heights in Sports",
        "description": "Join us at the Athlete's Ascent Summit, where sports enthusiasts and professionals converge to scale new heights in the world of athletics. This summit is a dynamic platform that transcends the ordinary, offering participants the chance to engage with sports legends, participate in interactive training sessions, and be inspired by stories of triumph and resilience. Whether you're an aspiring athlete or a dedicated fan, the Athlete's Ascent Summit promises an immersive experience that celebrates the spirit of competition, the pursuit of excellence, and the boundless potential within every athlete.",
        "date": datetime.strptime(fake.date(), '%Y-%m-%d').date(),
        "time": datetime.strptime(fake.time(), '%H:%M:%S').time(),
        "location": "Tokyo",
        "user_id": randint(1, 10),
        "image": "https://images.unsplash.com/photo-1461896836934-ffe607ba8211?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    },
    {
        "title": "TechCuisine Fusion: Where Technology Meets Culinary Art",
        "description": "Savor the innovative intersection of technology and culinary art at TechCuisine Fusion. This exceptional event invites attendees to explore the cutting-edge landscape of kitchen technology, from smart appliances to futuristic cooking techniques. Engage with chef-led tech-enhanced cooking demonstrations that showcase the seamless integration of technology and culinary creativity. TechCuisine Fusion is not just an exploration of gadgets; it's a culinary journey into the future, where technology enhances the art of cooking and transforms the way we experience gastronomy.",
        "date": datetime.strptime(fake.date(), '%Y-%m-%d').date(),
        "time": datetime.strptime(fake.time(), '%H:%M:%S').time(),
        "location": "California",
        "user_id": randint(1, 10),
        "image": "https://plus.unsplash.com/premium_photo-1663011236143-62855453066b?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    },
    {
        "title": "Adrenaline Rush Expo: Beyond the Ordinary in Extreme Sports",
        "description": "Experience the extraordinary at Adrenaline Rush Expo, where the thrill of extreme sports takes center stage. This expo goes beyond the ordinary, offering attendees the chance to witness adrenaline-pumping demonstrations, engage with extreme sports experts, and explore the latest innovations in the world of adventure. Whether you're a seasoned thrill-seeker or someone looking to discover the excitement of extreme sports, Adrenaline Rush Expo promises an immersive experience that pushes the boundaries of what's possible.",
        "date": datetime.strptime(fake.date(), '%Y-%m-%d').date(),
        "time": datetime.strptime(fake.time(), '%H:%M:%S').time(),
        "location": "Alaska",
        "user_id": randint(1, 10),
        "image": "https://images.unsplash.com/photo-1511264568880-afe3b1951e46?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    },
    {
        "title": "Vintner's Vision: A Celebration of Wine and Viticulture",
        "description": "Raise your glass to a celebration of wine and viticulture at Vintner's Vision. This unique event is a journey into the world of winemaking, featuring a curated selection of exceptional wines and the opportunity to connect with visionary winemakers. Explore the artistry behind each bottle, discover the intricacies of vineyard innovations, and indulge your palate in a tasting experience that uncorks the essence of the finest wines. Vintner's Vision is not just a celebration; it's a tribute to the craftsmanship, passion, and timeless allure of the world of wine.",
        "date": datetime.strptime(fake.date(), '%Y-%m-%d').date(),
        "time": datetime.strptime(fake.time(), '%H:%M:%S').time(),
        "location": "Madrid",
        "user_id": randint(1, 10),
        "image": "https://images.unsplash.com/photo-1547595628-c61a29f496f0?q=80&w=1374&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    },
    {
        "title": "Innovation Rally: Accelerating Progress in Multiple Arenas",
        "description": "Accelerate progress across multiple arenas at Innovation Rally, an extraordinary event that transcends traditional boundaries. From culinary delights to automotive marvels, sports breakthroughs, and beyond – this rally is a convergence of innovation that creates a unique fusion of ideas and experiences. Engage with thought leaders, explore the latest advancements, and be part of a movement that accelerates progress in various fields. Innovation Rally is not just an event; it's a rallying point for those passionate about shaping the future through groundbreaking ideas and collaborative efforts.",
        "date": datetime.strptime(fake.date(), '%Y-%m-%d').date(),
        "time": datetime.strptime(fake.time(), '%H:%M:%S').time(),
        "location": "Nairobi",
        "user_id": randint(1, 10),
        "image": "https://images.unsplash.com/photo-1589980763519-ddfa1c640d10?q=80&w=1487&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    }
]

with app.app_context():

    User.query.delete()
    Event.query.delete()
    Following.query.delete
    # Review.query.delete()
    # Follow.query.delete()
    # Attended.query.delete()


    for _ in range(10):
        user = User(
            username=fake.user_name(),
            password=fake.password(),
            email=fake.email(),
            image=fake.image_url(),
        )
        db.session.add(user)
        
    
    for event_data in events:
        event_instance = Event(**event_data)
        db.session.add(event_instance)


    pair1 = Following(
        id=1,
        user_id=5,
        event_id=8
        )
    db.session.add(pair1)
    

    for _ in range(10):
        review = Review(
            user_id=randint(1, 10),
            event_id=randint(1, 10),
            rating=fake.random_element(elements=(1.0, 2.0, 3.0, 4.0, 5.0)),
            comment=fake.text(),
        )
        db.session.add(review)

    for _ in range(10):
        attended = Attended(
            user_id=randint(1, 10),
            event_id=randint(1, 10),
        )
        db.session.add(attended)


    db.session.commit()


        # for _ in range(10):
    #     follow = Follow(
    #         user_id=randint(1, 10),
    #         event_id=randint(1, 10),
    #     )
    #     db.session.add(follow)

