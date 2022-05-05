import SwiftUI

struct RegisterView: View {
    @State private var name: String = ""
    @State private var email: String = ""
    @State private var password: String = ""
    
    var body: some View {
        
        NavigationView {
            Form {
                TextField("E-Mail", text: $name)
                TextField("Name", text: $name)
                SecureField("Password", text: $password)
                Button("Submit") {
                    print()
                }
            }
            .onSubmit {
                guard name.isEmpty == false && password.isEmpty == false else { return }
                print("test")
            }
            .navigationBarTitle("Register")
        }
    }
}
