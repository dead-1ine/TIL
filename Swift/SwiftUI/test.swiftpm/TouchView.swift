//
//  File.swift
//  test
//
//  Created by  yangws on 2022/05/05.
//

import SwiftUI

struct ContentView: View {
    @State var buttonPressed: Bool = false

    var body: some View {
        Text("Press to acccelerate")
            .foregroundColor(Color.white)
            .padding(10)
            .background(Color.gray)
            .cornerRadius(6)
            .padding(10)
            .scaleEffect(buttonPressed ? 0.8 : 1)
            .animation(.spring(), value: buttonPressed)
        
            .onTouchDownUp {
                pressed in self.buttonPressed = pressed
            }
    }
}

extension View {
    func onTouchDownUp(pressed: @escaping ((Bool) -> Void)) -> some View {
        self.modifier(TouchDownUpEventModifier(pressed: pressed))
    }
}

struct TouchDownUpEventModifier: ViewModifier {
    @State var dragged = false
    
    var pressed: (Bool) -> Void
    func body(content: Content) -> some View {
        content
            .gesture(
                DragGesture(minimumDistance: 0)
                    .onChanged { _ in
                        if !dragged {
                            dragged = true
                            pressed(true)
                        }
                    }
                    .onEnded { _ in dragged = false
                        pressed(false)
                    }
            )
    }
}
