### JAVA - MongoDrive
“자바에서 사용하는 MongoDB의 기능을 정리합니다.”

##### 1. Connect -\> DB -\> Colletion

1. Connection을 위한 인스턴스 생성
	```java
	MongoClient mongoClient = MongoClents.create();
	```

2. 데이터베이스 접근
	- 매개변수로 사용할 MongoDB의 데이터베이스 이름을 사용
	- (if) 지정한 이름의 DB가 존재하지 않으면, 데이터 저장 시 해당 이름의 데이터베이스를 생성
	```java
	MongoDatabase database = mongoClient.getDatabase("DB이름");
	```

3. Collection 접근
	- 데이터베이스와 마찬가지로 지정한 이름의 Collection이 존재하지 않을 경우, 데이터 저장 시 해당 이름의 Collection을 생성
	```java
	MongoCollection<Document> collection = database.getCollection("Collection이름");
	```

---- 
##### 2. Insert Documents on MongoDB

1. Document 만들기
	- Document : 문서를 만들기 위한 클래스
	```java
	Document doc = new Document("name", "MongoDB")
					.append("type", "database")
					.append("count", 1);

	// 값이 배열 형태로 존재할 경우 asList() 메소드를 이용
	doc.append("versions", Arrays.asList("v3.2", "v3.0", "v2.6"));

	// 하위 필드가 존재할 경우 new Document 객체를 만들어 필드의 값으로 넣음
	doc.append("info", new Document("x", 203).append("y", 102));

	/* 위 내용으로 만든 JSON
		{
			"name" : "MongoDB",
			"type" : "database",
			"count" : 1,
			"versions" : [ "v3.2", "v3.0", "v2.6" ],
			"info" : { x : 203, y : 102 }
		}
	*/
	```

2. Insert Document
	- insertOne(Document) : 하나의 문서를 저장
	```java
	collection.insertOne(doc);
	```

3. Insert Documents
	- insertMany(ArrayList\<Document\>) : 여러 개의 문서를 저장
	```java
	List<Document> documents = new ArrayList<>();
	for (int i = 0; i < 100; i++) {
		documents.add(new Document("i", i));
	}
	collection.insertMany(documents);
	```
