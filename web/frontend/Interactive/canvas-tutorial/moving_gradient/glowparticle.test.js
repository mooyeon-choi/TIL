const glowparticle = require("./glowparticle")

// @ponicode
describe("animate", () => {
    let inst

    beforeEach(() => {
        inst = new glowparticle.GlowParticle(520, 70, 0.01, "green")
    })

    test("0", () => {
        let callFunction = () => {
            inst.animate({ fillStyle: { addColorStop: () => "da7588892" }, beginPath: () => "path/to/file.ext", createRadialGradient: () => false, arc: () => 4, fill: () => true }, 12, 99)
        }
    
        expect(callFunction).not.toThrow()
    })

    test("1", () => {
        let callFunction = () => {
            inst.animate({ fillStyle: { addColorStop: () => 12345 }, beginPath: () => "path/to/folder/", createRadialGradient: () => false, arc: () => 410, fill: () => false }, "a1969970175", 48000)
        }
    
        expect(callFunction).not.toThrow()
    })

    test("2", () => {
        let callFunction = () => {
            inst.animate({ fillStyle: { addColorStop: () => 9876 }, beginPath: () => "path/to/file.ext", createRadialGradient: () => true, arc: () => 350, fill: () => true }, 12, 480)
        }
    
        expect(callFunction).not.toThrow()
    })

    test("3", () => {
        let callFunction = () => {
            inst.animate({ fillStyle: { addColorStop: () => "c466a48309794261b64a4f02cfcc3d64" }, beginPath: () => "C:\\\\path\\to\\folder\\", createRadialGradient: () => false, arc: () => 100, fill: () => true }, 987650, 255)
        }
    
        expect(callFunction).not.toThrow()
    })

    test("4", () => {
        let callFunction = () => {
            inst.animate({ fillStyle: { addColorStop: () => "c466a48309794261b64a4f02cfcc3d64" }, beginPath: () => "path/to/folder/", createRadialGradient: () => true, arc: () => 400, fill: () => false }, "a1969970175", 100)
        }
    
        expect(callFunction).not.toThrow()
    })

    test("5", () => {
        let callFunction = () => {
            inst.animate({}, Infinity, undefined)
        }
    
        expect(callFunction).not.toThrow()
    })
})
