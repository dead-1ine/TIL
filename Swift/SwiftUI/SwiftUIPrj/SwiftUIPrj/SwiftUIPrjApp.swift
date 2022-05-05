//
//  SwiftUIPrjApp.swift
//  SwiftUIPrj
//
//  Created by  yangws on 2022/05/05.
//

import SwiftUI

@main
struct SwiftUIPrjApp: App {
    let persistenceController = PersistenceController.shared

    var body: some Scene {
        WindowGroup {
            ContentView()
                .environment(\.managedObjectContext, persistenceController.container.viewContext)
        }
    }
}
